
# this is a main code that would receive angles from site
# then move the arm
#
import config
import wifi_connect
from recv_angles import recv_on
from arm import Arm
from machine import Pin


# 
#
def main():
    # get the host and port 
    # 
    HOST = wifi_connect.connect(ssid=config.SSID, password=config.PASS)
    PORT = 5001
    
    # create the arm object
    #
    ARM_FLAG = 1
    arm = Arm()
    
    # turn on the LED to know it's ready to recv angles
    # TODO: this is a flag that is going to be sent to the PI
    #
    LED_PIN = 25 
    led = Pin(LED_PIN, Pin.OUT)
    led.value(ARM_FLAG)
    
 
    
    # receive first set of angles
    #
    angles = recv_on(host=HOST, port=PORT)

    while True:
        print("angles are = {}".format(angles))
        
        # turn off the LED meaning the arm is moving
        #
        led.value(not ARM_FLAG)
        
        # move the arn
        # 
        ARM_FLAG = arm.moveJoints(angles=angles)
        
                
        # turn on the LED meaning the arm is ready to receive
        #
        led.value(ARM_FLAG)
        
        # recv next set of angles
        #
        angles = recv_on(host=HOST, port=PORT)

if __name__ == "__main__":
    pass