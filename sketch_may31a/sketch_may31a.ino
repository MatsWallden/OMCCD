String message="";
double a=0.0;
void setup(){
  Serial.begin(9600);
}
void loop(){
  if(Serial.available()>0){
    message=Serial.readString(); //READS INSTRUCTION
    a=atof(message.c_str())+1;
    Serial.println(a);      
  } 

}



