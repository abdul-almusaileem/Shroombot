#include <SoftwareSerial.h>

//
//
#define GET_LOW_BYTE(A) (uint8_t)((A))
//宏函数 获得A的低八位
//
#define GET_HIGH_BYTE(A) (uint8_t)((A) >> 8)
//宏函数 获得A的高八位
//
#define BYTE_TO_HW(A, B) ((((uint16_t)(A)) << 8) | (uint8_t)(B))
//宏函数 以A为高八位 B为低八位 合并为16位整形
//
#define LOBOT_SERVO_FRAME_HEADER         0x55
#define LOBOT_SERVO_MOVE_TIME_WRITE      1
#define LOBOT_SERVO_ID_WRITE             13


// number of servos used
//
#define NUM_SERVOS 2


// create the servo opjects
//
//SoftwareSerial servo_1(5, 6);
//SoftwareSerial servo_2(7, 8);

// create an array of servos
//
//SoftwareSerial servos[NUM_SERVOS] = {servo_1, servo_2};

// input values to move the servos
//
int16_t servo;
int16_t position;

// function prototypes
//
void servos_init(SoftwareSerial servos[]);
byte LobotCheckSum(byte buf[]);
void servo_set_id(SoftwareSerial &SerialX, uint8_t oldID, uint8_t newID);
void servo_move(SoftwareSerial &SerialX, uint8_t id, int16_t position,
                uint16_t time);


//
//
void setup() {
    // initial Harsware Serial for serial input
    //
    Serial.begin(9600);
    delay(1000);

    // initialize the servoes using the SoftwareSerial
    //
    //servos_init(servos);
    
    delay(1000);
}

void loop() {
/*
    while (Serial.available()) {
        // read which servo and what position to move it
        //
        servo = Serial.parseInt();
        position = Serial.parseInt();

        // move the picked servoe to the specified position
        //
        switch (servo) {
            case 1:
                Serial.print("first motor -> ");
                Serial.println(position);
                servo_move(servo_1, 1, position, 1000);
                break;
            case 2:
                Serial.print("second motor -> ");
                Serial.println(position);
                servo_move(servo_2, 1, position, 1000);
                break;
            default:
                Serial.println("Undeclared Servo");
                continue;
        }
        delay(2000);
    }
    */

    LobotSerialServoMove(serial)
}

/*
// initialize all the servos that wehave
//
void servos_init(SoftwareSerial servo[]) {
    for (int i = 0; i < NUM_SERVOS; i++) {
        servos[i].begin(115200);
        servo_set_id(servos[i], 254, 1);
        Serial.println(i);
    }
}
*/

// checksum
// TODO: HOW DOES IT WORK
//
byte LobotCheckSum(byte buf[])   //校验数据
{
  byte i;
  uint16_t temp = 0;
  for (i = 2; i < buf[3] + 2; i++) {
    temp += buf[i];
  }
  temp = ~temp;
  i = (byte)temp;
  return i;
}
/*
//
//
void servo_set_id(SoftwareSerial &SerialX, uint8_t oldID, uint8_t newID) {
  byte buf[7];
  buf[0] = buf[1] = LOBOT_SERVO_FRAME_HEADER;
  buf[2] = oldID;
  buf[3] = 4;
  buf[4] = LOBOT_SERVO_ID_WRITE;
  buf[5] = newID;
  buf[6] = LobotCheckSum(buf);
  SerialX.write(buf, 7);
}

//
//
void servo_move(SoftwareSerial &SerialX, uint8_t id, int16_t position,
                uint16_t time)  {
  byte buf[10];
  if(position < 0)
    position = 0;
  if(position > 1000)
    position = 1000;
  buf[0] = buf[1] = LOBOT_SERVO_FRAME_HEADER;
  buf[2] = id;
  buf[3] = 7;
  buf[4] = LOBOT_SERVO_MOVE_TIME_WRITE;
  buf[5] = GET_LOW_BYTE(position);
  buf[6] = GET_HIGH_BYTE(position);
  buf[7] = GET_LOW_BYTE(time);
  buf[8] = GET_HIGH_BYTE(time);
  buf[9] = LobotCheckSum(buf);
  SerialX.write(buf, 10);
}
*/


// hardware serial
//

//
//
void LobotSerialServoMove(HardwareSerial &SerialX, uint8_t id, int16_t position,
                         uint16_t time)  //设置舵机转动
{
  byte buf[10];
  if(position < 0)
    position = 0;
  if(position > 1000)
    position = 1000;
  buf[0] = buf[1] = LOBOT_SERVO_FRAME_HEADER;
  buf[2] = id;
  buf[3] = 7;
  buf[4] = LOBOT_SERVO_MOVE_TIME_WRITE;
  buf[5] = GET_LOW_BYTE(position);
  buf[6] = GET_HIGH_BYTE(position);
  buf[7] = GET_LOW_BYTE(time);
  buf[8] = GET_HIGH_BYTE(time);
  buf[9] = LobotCheckSum(buf);
  SerialX.write(buf, 10);
}

//
//
void LobotSerialServoSetID(HardwareSerial &SerialX, uint8_t oldID, uint8_t newID)
{
  byte buf[7];
  buf[0] = buf[1] = LOBOT_SERVO_FRAME_HEADER;
  buf[2] = oldID;
  buf[3] = 4;
  buf[4] = LOBOT_SERVO_ID_WRITE;
  buf[5] = newID;
  buf[6] = LobotCheckSum(buf);
  SerialX.write(buf, 7);
}
