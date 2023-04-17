int i = 0;
void setup()
{
  Serial.begin(9600);
  int x_diff, y_diff = 100, -50;
  int t = 0.2;

  while (true)
  { if (abs(x_diff) > t && abs(y_diff) > t)
    { 
      if ((x_diff > 0) && (y_diff > 0)) {
        x_diff--;
        y_diff--;

      }
      if ((x_diff > 0) &&(y_diff < 0)) {
        x_diff--;
        y_diff++;

      }
      if ((x_diff < 0) && (y_diff > 0)) {
        x_diff++;
        y_diff--;

      }
      if ((x_diff < 0) && (y_diff < 0)) {
        x_diff++;
        y_diff++;

      }
    }
    else if(abs(x_diff)>t && abs(y_diff)<t){
      if ((x_diff > 0)) {
        x_diff--;
        

      }
      if ((x_diff < 0)) {
        x_diff++;

      }
      
    }
    else if(abs(x_diff)<t && abs(y_diff)>t){
      if ((y_diff > 0)) {
        y_diff--;
        

      }
      if ((y_diff < 0)) {
        y_diff++;

      }
      
    }
    else{
      Serial.println("Differences already in threshold");
      
    }
  }
  Serial.println("The number of iterations is ");
  Serial.println(i);
}
void loop()
{}