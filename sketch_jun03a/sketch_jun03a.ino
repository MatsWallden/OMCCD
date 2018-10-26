void setup(){
Serial.begin(9600);
pinMode(5,INPUT);
}
void loop(){
Serial.println(pulseIn(5,HIGH));
}
