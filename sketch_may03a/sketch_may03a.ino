int x{0};
int y{0};
void setup(){
Serial.begin(9600);

}

void loop(){
  //x=Serial.available();
  while(Serial.available()==0){}
  y=Serial.parseInt();
  Serial.println(y+1);  
}

