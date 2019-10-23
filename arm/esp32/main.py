
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
from dist_ping import get_distance
from send_dist import send_dist

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
    
    Z_FLAG = 0
    
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
            angles, addr = recv_on(host=HOST, port=PORT)
 
            print("angles are = {}".format(angles))
            
            print("addr {}".format(addr))
        
            # turn off the LED meaning the arm is moving
            #
            led.value(not ARM_FLAG)
        
            # move the arn
            # 
            ARM_FLAG = arm.moveJoints(angles=angles)

            # if angles is not empty flag_z = True
            #
            if (len(angles) > 0):
                Z_FLAG = 1
            else:
                Z_FLAG = 0
            
            
            # if flag_z:
            # send Z to pi via socket
            #
            if Z_FLAG:
                # 
                #
                num_samples = 10
                mushroom_dist = 0
                for _ in range(0, num_samples):
                    mushroom_dist = mushroom_dist +  get_distance(27)
                
                mushroom_dist = mushroom_dist / num_samples
                print("dist: {}".format(mushroom_dist))
                send_dist(mushroom_dist, addr=addr[0], port=5002)
                Z_FLAG = 0
                
            print("sent Z, recputing")
            sleep(1)
            angles, addr = recv_on(host=HOST, port=PORT)
            ARM_FLAG = arm.moveJoints(angles=angles)

            print("GOT THE THING")

if __name__ == "__main__":
    main()



