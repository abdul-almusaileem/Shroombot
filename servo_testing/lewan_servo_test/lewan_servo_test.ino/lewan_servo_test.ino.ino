


/*
    mid_points = {  1: 450,
                    2: 450,
                    3: 675,
                    4: 275
                }
*/

// TODO: 1) write the begin & and the idle functions.
// TODO: 2) send the values at once and maybe move at once too.
// TODO: 3) control with some sort of controller.
// TODO: 4)
//


//
//
#include <SoftwareSerial.h>
// split the 16bit to two 8bit cars concat the the upper and lower bits
//
#define GET_LOW_BYTE(A) (uint8_t)((A))
#define GET_HIGH_BYTE(A) (uint8_t)((A) >> 8)
#define BYTE_TO_HW(A, B) ((((uint16_t)(A)) << 8) | (uint8_t)(B))
#define LOBOT_SERVO_FRAME_HEADER         0x55
#define LOBOT_SERVO_MOVE_TIME_WRITE      1
#define LOBOT_SERVO_ID_WRITE             13


// number of servos used
//
#define NUM_SERVOS 4


// creatte the SoftwareSerial objects
// SoftwareSerial serial(Tx, Rx)
// we are using the Rx pins
//
SoftwareSerial servo_1(1, 2);
SoftwareSerial servo_2(3, 4);
SoftwareSerial servo_3(5, 6);
SoftwareSerial servo_4(7, 8);

// create an array of servos
//
SoftwareSerial servos[NUM_SERVOS] = {servo_1, servo_2, servo_3, servo_4};

// input values to move the servos
//
int16_t servo;
int16_t position;

// function prototypes
//
void servos_begin(SoftwareSerial servos[]);
void servos_idle(SoftwareSerial servos[]);
void servo_set_id(SoftwareSerial &SerialX, uint8_t oldID, uint8_t newID);
void servo_move(SoftwareSerial &SerialX, uint8_t id, int16_t position,
                uint16_t time);
byte LobotCheckSum(byte buf[]);


//
//
void setup() {
    // initial Harsware Serial for serial input
    //
    Serial.begin(9600);
    delay(1000);

    // TODO: delete this and just use the servos_begin
    //
    servo_1.begin(115200);
    servo_2.begin(115200);
    servo_3.begin(115200);
    servo_4.begin(115200);
    servo_set_id(servo_1, 254, 1);
    servo_set_id(servo_2, 254, 1);
    servo_set_id(servo_3, 254, 1);
    servo_set_id(servo_4, 254, 1);


    // initialize the servoes using the SoftwareSerial
    // FIXME: Try to make it work to look neat...
    //
    //servos_begin(servos);
}

void loop() {

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
                case 3:
                Serial.print("Third motor -> ");
                Serial.println(position);
                servo_move(servo_3, 1, position, 1000);
                break;

            case 4:
                Serial.print("Fourth motor -> ");
                Serial.println(position);
                servo_move(servo_4, 1, position, 1000);
                break;
            default:
                Serial.println("Undeclared Servo");
                continue;
        }
        delay(2000);
    }
}


// initialize all the servos that wehave
// TODO: add led to announce the that the init finished 
//
void servos_begin(SoftwareSerial servo[]) {
    for (int i = 0; i < NUM_SERVOS-1; i++) {
        servo[i].begin(115200);
        servo_set_id(servo[i], 254, 1);
        delay(1000);
    }
}

// puts the arm into IDLE position
// TODO: make it work!!
void servos_idle(SoftwareSerial servos[]) {

}

// set the servo's ID
// TODO: HOW DOES IT WORK
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

// move the servo to a specified position
// TODO: HOW DOES IT WORK
// TODO: play with time var
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

// checksum to make sure that the packet was sent
// TODO: HOW DOES IT WORK
//
byte LobotCheckSum(byte buf[]) {
  byte i;
  uint16_t temp = 0;
  for (i = 2; i < buf[3] + 2; i++) {
    temp += buf[i];
  }
  temp = ~temp;
  i = (byte)temp;
  return i;
}
