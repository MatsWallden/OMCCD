void setup(){
Serial.begin(9600);
}

void loop(){
if(Serial.available()>0){
  if(Serial.readString()=="*IDN?"{
    Serial.println(
      Serial.println("ARDUINO UNO")){
      }
    )
  }
}
