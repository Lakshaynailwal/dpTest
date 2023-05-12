# String cmd;
# #include<Servo.h>

# Servo servoTopToBottom;
# Servo servoLeftToRight;

# int th = 10; //threshold
# int deg = 180;
# int val = 50;
# bool flagToTorch = false;

# void getData(float &x1 , float &y1){

#   // 28.5 + 29.0
#   cmd = Serial.readString();
  
#   String x_diff = "";
#   String x = "";
#   String y_diff = "";
#   for ( int i = 0; i<cmd.length() ;i++){
#     if( cmd[i] != ' '){
#       if( cmd[i] != '+' ){
#         x_diff = x_diff + cmd[i];
#       }
#       else{
#         x = x_diff;
#         x_diff = "";
#       }
#     }
#   }

#   y_diff = x_diff;
#   x_diff = x;

#   x1 = x_diff.toFloat();
#   y1 = y_diff.toFloat();
  
# }

# void setup()
# {
#   Serial.begin(115200);
#   pinMode(3 , OUTPUT); // --> servoLeftToRight
#   pinMode(5 , OUTPUT); // --> servoTopToBottom
#   pinMode(LED_BUILTIN , OUTPUT); // --> Led
  
#   servoTopToBottom.attach(3);
#   servoLeftToRight.attach(5);
  
# }

# void loop() {

#   while ( Serial.available() == 0) {
#      servoLeftToRight.write(deg);
#      servoTopToBottom.write(deg);
#   }

#   // if getting data  
#   while(true){
#     float X = 0;
#     float Y = 0;
    
#     getData(X,Y);
#     if( abs(X) > th && abs(Y) > th){
#        flagToTorch = false;
#        if( X>0 && Y>0 ){
        
#         if(deg-val >= 0){
#           servoLeftToRight.write(deg-=val);
#           servoTopToBottom.write(deg-=val);
#         }
#         else{
#           deg = 180;
#           servoLeftToRight.write(deg-=val);
#           servoTopToBottom.write(deg-=val);
#         }
        
#        }
#        else if(X>0 && Y<0){

#         if(deg+val <= 180)
#           servoTopToBottom.write(deg+=val);
#         else{
#           deg = 0; 
#           servoTopToBottom.write(deg+=val); 
#         }

#         if(deg-val >= 0)
#           servoLeftToRight.write(deg-=val);
#         else{
#           deg = 180;
#           servoLeftToRight.write(deg-=val);
#         }
#        }
#        else if(X<0 && Y>0){
#         if(deg-val <= 180)
#           servoLeftToRight.write(deg+=val);
#         else{
#           deg = 0;
#           servoLeftToRight.write(deg+=val);
#         }

#         if(deg-val >= 0)
#           servoTopToBottom.write(deg-=val);
#         else{
#           deg = 180;
#           servoTopToBottom.write(deg-=val);
#         }
            
#        }
#        else{
#         if(deg-val <= 180){
#           servoLeftToRight.write(deg+=val);
#           servoTopToBottom.write(deg+=val);
#         }
#         else{
#           deg = 0;
#           servoLeftToRight.write(deg+=val);
#           servoTopToBottom.write(deg+=val);
#         }
        
#        }     
#     }
#     else if(abs(X)>th && abs(Y)<th){
#       flagToTorch = false;
#       if(X > 0){
#         if(deg-val >= 0)
#           servoLeftToRight.write(deg-=val);
#         else{
#           deg = 180;
#           servoLeftToRight.write(deg-=val);  
#         }
#       }
#       else{
#         if(deg-val <= 180)
#           servoLeftToRight.write(deg+=val);
#         else{
#           deg = 0;
#           servoLeftToRight.write(deg+=val);
#         }
#       }
#     }
#     else if(abs(X)<th && abs(Y)>th){
#       flagToTorch = false;
#       if(Y > 0){

#         if(deg-val >=0)
#           servoTopToBottom.write(deg-=val);
#         else{
#           deg = 180; 
#           servoTopToBottom.write(deg-=val); 
#         }
#       }
#       else{

#         if(deg-val <=180)
#           servoTopToBottom.write(deg+=val);
#         else{
#           deg = 0;
#           servoTopToBottom.write(deg+=val);
#         }
#       }
#     }

#     else{
#       flagToTorch = true;
#     }

#     if(flagToTorch){
#       digitalWrite(LED_BUILTIN, HIGH);
#     }
#     else{
#       digitalWrite(LED_BUILTIN, LOW);
#     }
#   }
# }
#!/usr/bin/python3
import OPi.GPIO as GPIO
from time import sleep

# #piny podle civek
# c11 = 37
# c12 = 35
# c21 = 33
# c22 = 31

# #funkce pro pohyb (jeden cyklus)
# def fw(delay):
#     GPIO.output(c11, 0)
#     GPIO.output(c12, 1)
#     sleep(delay)
#     GPIO.output(c12, 0)

#     GPIO.output(c21, 0)
#     GPIO.output(c22, 1)
#     sleep(delay)
#     GPIO.output(c22, 0)

#     GPIO.output(c11, 1)
#     GPIO.output(c12, 0)
#     sleep(delay)
#     GPIO.output(c11, 0)

#     GPIO.output(c21, 1)
#     GPIO.output(c22, 0)
#     sleep(delay)
#     GPIO.output(c21, 0)

# def bw(delay):
#     GPIO.output(c21, 1)
#     GPIO.output(c22, 0)
#     sleep(delay)
#     GPIO.output(c21, 0)

#     GPIO.output(c11, 1)
#     GPIO.output(c12, 0)
#     sleep(delay)
#     GPIO.output(c11, 0)

#     GPIO.output(c21, 0)
#     GPIO.output(c22, 1)
#     sleep(delay)
#     GPIO.output(c22, 0)

#     GPIO.output(c11, 0)
#     GPIO.output(c12, 1)
#     sleep(delay)
#     GPIO.output(c12, 0)

# def setup():
#     GPIO.setboard(GPIO.PCPCPLUS)
#     GPIO.setmode(GPIO.BOARD)

#     for pin in [c11, c12, c21, c22]:
#         GPIO.setup(pin, GPIO.OUT)

# def cleanup():
#     for pin in [c11, c12, c21, c22]:
#         GPIO.output(pin, 0)
#     GPIO.cleanup()
import OPi.GPIO as GPIO
from time import sleep

from time import sleep
import sys

#assign GPIO pins for motor
motor_channel = (29,31,33,35)  
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
#for defining more than 1 GPIO channel as input/output use
GPIO.setup(motor_channel, GPIO.OUT)

motor_direction = input('select motor direction a=anticlockwise, c=clockwise: ')
while True:
    try:
        if(motor_direction == 'c'):
            print('motor running clockwise\n')
            GPIO.output(motor_channel, (GPIO.HIGH,GPIO.LOW,GPIO.LOW,GPIO.HIGH))
            sleep(0.02)
            GPIO.output(motor_channel, (GPIO.HIGH,GPIO.HIGH,GPIO.LOW,GPIO.LOW))
            sleep(0.02)
            GPIO.output(motor_channel, (GPIO.LOW,GPIO.HIGH,GPIO.HIGH,GPIO.LOW))
            sleep(0.02)
            GPIO.output(motor_channel, (GPIO.LOW,GPIO.LOW,GPIO.HIGH,GPIO.HIGH))
            sleep(0.02)

        elif(motor_direction == 'a'):
            print('motor running anti-clockwise\n')
            GPIO.output(motor_channel, (GPIO.HIGH,GPIO.LOW,GPIO.LOW,GPIO.HIGH))
            sleep(0.02)
            GPIO.output(motor_channel, (GPIO.LOW,GPIO.LOW,GPIO.HIGH,GPIO.HIGH))
            sleep(0.02)
            GPIO.output(motor_channel, (GPIO.LOW,GPIO.HIGH,GPIO.HIGH,GPIO.LOW))
            sleep(0.02)
            GPIO.output(motor_channel, (GPIO.HIGH,GPIO.HIGH,GPIO.LOW,GPIO.LOW))
            sleep(0.02)

            
    #press ctrl+c for keyboard interrupt
    except KeyboardInterrupt:
        #query for setting motor direction or exit
        motor_direction = input('select motor direction a=anticlockwise, c=clockwise or q=exit: ')
        #check for exit
        if(motor_direction == 'q'):
            print('motor stopped')
            sys.exit(0)