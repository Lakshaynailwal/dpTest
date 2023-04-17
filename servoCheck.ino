String cmd;
#include<Servo.h>

Servo servoTopToBottom;
Servo servoLeftToRight;

int th = 10; //threshold
int deg = 180;
int val = 50;
bool flagToTorch = false;

void getData(float &x1 , float &y1){

  // 28.5 + 29.0
  cmd = Serial.readString();
  
  String x_diff = "";
  String x = "";
  String y_diff = "";
  for ( int i = 0; i<cmd.length() ;i++){
    if( cmd[i] != ' '){
      if( cmd[i] != '+' ){
        x_diff = x_diff + cmd[i];
      }
      else{
        x = x_diff;
        x_diff = "";
      }
    }
  }

  y_diff = x_diff;
  x_diff = x;

  x1 = x_diff.toFloat();
  y1 = y_diff.toFloat();
  
}

void setup()
{
  Serial.begin(115200);
  pinMode(3 , OUTPUT); // --> servoLeftToRight
  pinMode(5 , OUTPUT); // --> servoTopToBottom
  pinMode(LED_BUILTIN , OUTPUT); // --> Led
  
  servoTopToBottom.attach(3);
  servoLeftToRight.attach(5);
  
}

void loop() {

  while ( Serial.available() == 0) {
     servoLeftToRight.write(deg);
     servoTopToBottom.write(deg);
  }

  // if getting data  
  while(true){
    float X = 0;
    float Y = 0;
    
    getData(X,Y);
    if( abs(X) > th && abs(Y) > th){
       flagToTorch = false;
       if( X>0 && Y>0 ){
        
        if(deg-val >= 0){
          servoLeftToRight.write(deg-=val);
          servoTopToBottom.write(deg-=val);
        }
        else{
          deg = 180;
          servoLeftToRight.write(deg-=val);
          servoTopToBottom.write(deg-=val);
        }
        
       }
       else if(X>0 && Y<0){

        if(deg+val <= 180)
          servoTopToBottom.write(deg+=val);
        else{
          deg = 0; 
          servoTopToBottom.write(deg+=val); 
        }

        if(deg-val >= 0)
          servoLeftToRight.write(deg-=val);
        else{
          deg = 180;
          servoLeftToRight.write(deg-=val);
        }
       }
       else if(X<0 && Y>0){
        if(deg-val <= 180)
          servoLeftToRight.write(deg+=val);
        else{
          deg = 0;
          servoLeftToRight.write(deg+=val);
        }

        if(deg-val >= 0)
          servoTopToBottom.write(deg-=val);
        else{
          deg = 180;
          servoTopToBottom.write(deg-=val);
        }
            
       }
       else{
        if(deg-val <= 180){
          servoLeftToRight.write(deg+=val);
          servoTopToBottom.write(deg+=val);
        }
        else{
          deg = 0;
          servoLeftToRight.write(deg+=val);
          servoTopToBottom.write(deg+=val);
        }
        
       }     
    }
    else if(abs(X)>th && abs(Y)<th){
      flagToTorch = false;
      if(X > 0){
        if(deg-val >= 0)
          servoLeftToRight.write(deg-=val);
        else{
          deg = 180;
          servoLeftToRight.write(deg-=val);  
        }
      }
      else{
        if(deg-val <= 180)
          servoLeftToRight.write(deg+=val);
        else{
          deg = 0;
          servoLeftToRight.write(deg+=val);
        }
      }
    }
    else if(abs(X)<th && abs(Y)>th){
      flagToTorch = false;
      if(Y > 0){

        if(deg-val >=0)
          servoTopToBottom.write(deg-=val);
        else{
          deg = 180; 
          servoTopToBottom.write(deg-=val); 
        }
      }
      else{

        if(deg-val <=180)
          servoTopToBottom.write(deg+=val);
        else{
          deg = 0;
          servoTopToBottom.write(deg+=val);
        }
      }
    }

    else{
      flagToTorch = true;
    }

    if(flagToTorch){
      digitalWrite(LED_BUILTIN, HIGH);
    }
    else{
      digitalWrite(LED_BUILTIN, LOW);
    }
  }
}
