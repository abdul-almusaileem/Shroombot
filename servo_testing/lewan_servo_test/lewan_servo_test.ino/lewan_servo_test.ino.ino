#include <ServoLX.h>

int rx = 8;
int tx = 7;

ServoLX servo(rx, tx);

int id;

void setup()
{
 // activate the motor serial connection
 //
 //
 servo.begin();
 Serial.begin(115200);

 // initial stop the motor
 //
 servo.disable();

}

void loop()
{
    id = 1;
    servo.setid(id);
    servo.enable();
    //int pos = servo.position_raw(id);
	//Serial.println(pos);

  //servo.position_raw(id);

  servo.move(id, 10.3);
  servo.start();

  servo.move_raw(id, 500);
  servo.start();

  Serial.println("nothing yet...");
  delay(1000);
}
