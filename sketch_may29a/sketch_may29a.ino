//String BLA='';
void setup(){
  Serial.begin(9600);
}
void  loop(){
  Serial.println(Serial.readString());
  delay(10);
}

