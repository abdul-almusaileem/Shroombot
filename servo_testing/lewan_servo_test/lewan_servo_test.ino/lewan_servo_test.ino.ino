#include <ServoLX.h>

int rx = 9;
int tx = 7;

ServoLX servo(rx, tx);

int id;

void setup()
{
 // activate the motor serial connection
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
    id -= '0' + 0x0;
    servo.setid(id);
    servo.enable(id);
    Serial.println(servo.getid());
    int pos = servo.position_raw(id);
	//Serial.println(pos);

  //servo.position_raw(id);

  //servo.move(id, 500);

  //servo.start();

  delay(1000);
}
