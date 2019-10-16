
# this is a main code that would receive angles from site
# then move the arm
#
import config
import wifi_connect
from recv_angles import recv_on
from arm import Arm
from machine import Pin
import network
from time import sleep

# 
#
def main():

    station = network.WLAN(network.STA_IF)

    WIFI_LED_PIN = 26
    wifi_led = Pin(WIFI_LED_PIN, Pin.OUT)

    # check if no wifi connection
    #
    if not station.isconnected():
        wifi_led.value(0)

        
    # get the host and port 
    # 
    HOST = wifi_connect.connect(ssid=config.SSID, password=config.PASS)
    PORT = 5001

    # check if connection has been established
    #
    if station.isconnected():
        wifi_led.value(1)
    
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
    
    # flash blue led to check
    #
    sleep(0.5)
    led.value(1)
    sleep(0.5)
    led.value(0)
    sleep(0.5)
    
    # FIXME: find out the problem with the blue led
    #
    while True:
        
        # check if no wifi connection                                                   
        #
        if not station.isconnected():
            print("wifi disconnected...")
            wifi_led.value(0)
            led.value(0)

            # this will loop foreever until wifi is here
            #
            HOST = wifi_connect.connect(ssid=config.SSID, password=config.PASS)

        else:
            wifi_led.value(1)
            
            # turn on the LED meaning the arm is ready to receive
            #
            led.value(ARM_FLAG)
            angles = recv_on(host=HOST, port=PORT)
 
            print("angles are = {}".format(angles))
        
            # turn off the LED meaning the arm is moving
            #
            led.value(not ARM_FLAG)
        
            # move the arn
            # 
            ARM_FLAG = arm.moveJoints(angles=angles)

  

if __name__ == "__main__":
    main()



