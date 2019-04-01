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

int dir = 0;
int flag = 0;

SoftwareSerial motor(10, 11);

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

void LobotSerialServoMove(HardwareSerial &SerialX, uint8_t id, int16_t position, uint16_t time)  //设置舵机转动
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

void LobotSerialServoSetID(HardwareSerial &SerialX, uint8_t oldID, uint8_t newID)    //设置舵机号
{
  byte buf[7];
  buf[0] = buf[1] = LOBOT_SERVO_FRAME_HEADER;
  buf[2] = oldID;
  buf[3] = 11;
  buf[4] = LOBOT_SERVO_ID_WRITE;
  buf[5] = newID;
  buf[6] = LobotCheckSum(buf);
  SerialX.write(buf, 7);
}



void LobotSerialServoSetID_software(SoftwareSerial &SerialX, uint8_t oldID, uint8_t newID)    //设置舵机号
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

void setup() {
  // put your setup code here, to run once:
  // put your setup code here, to run once:
  //


  byte buf[7];
  buf[0] = buf[1] = LOBOT_SERVO_FRAME_HEADER;
  buf[2] = 0xFE;       // id
  buf[3] = 0x4;
  buf[4] = 0x13;
  buf[5] = 0x2;
  buf[6] = LobotCheckSum(buf);
  Serial.write(buf, 7);




  Serial.begin(115200);  //初始化波特率
  delay(1000);
  //LobotSerialServoSetID(Serial, 1, 2);   //设置所有舵机为1号舵机
  //LobotSerialServoSetID_software(motor, 254, 2);   //设置所有舵机为1号舵机
  delay(1000);
}

void loop() {
  // put your main code here, to run repeatedly:
  //
 // LobotSerialServoMove(Serial, 1, dir, 1000);   //使1号舵机用500ms的时间转动到100的位置
//    delay(2000);  //延时，等待舵机运行
  //LobotSerialServoMove(Serial, 1, 700, 1000);   //使1号舵机用500ms的时间转动到500的位置
    //delay(2000);  //延时，等待舵机运行


    byte buf[7];
    buf[0] = buf[1] = LOBOT_SERVO_FRAME_HEADER;
    buf[2] = 0xFE;       // id
    buf[3] = 0x4;
    buf[4] = 0x13;
    buf[5] = 0x2;
    buf[6] = LobotCheckSum(buf);
    Serial.write(buf, 7);


    LobotSerialServoMove(Serial,2, 500, 1000);   //使1号舵机用500ms的时间转动到100的位置
    delay(2000);



    //LobotSerialServoMove(Serial, 2, 500, 1000);   //使1号舵机用500ms的时间转动到100的位置
    //delay(2000);

    //LobotSerialServoMove(Serial, 2, 1000, 1000);   //使1号舵机用500ms的时间转动到100的位置
    //delay(2000);

    LobotSerialServoMove(Serial, 2, 0, 1000);   //使1号舵机用500ms的时间转动到100的位置
    delay(2000);

    Serial.println("");
    Serial.println(dir);
}
