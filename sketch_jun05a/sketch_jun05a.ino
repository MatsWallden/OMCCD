#include <Wire.h>

void setup(){
Wire.begin(0x00);
Wire.onRequest(requestEvent);
Serial.begin(9600);
}
void loop(){
Serial.println("LOOP");
delay(10);
}

void requestEvent(){
Wire.write("1");
}
