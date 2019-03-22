#include <ServoLX.h>

int rx = 7;
int tx = 8;

ServoLX servo(rx, tx);
int id;
  
void setup()
{  
 id = servo.getid();
 servo.setid(id);
 servo.enable();
 //servo.begin();
 Serial.begin(115200);
 //servo.disable();
}

void loop()
{
  int pos = servo.position_raw(id);
    Serial.println(pos);
    
  servo.move(id, -40);
  //servo.begin();
  servo.start();
}

