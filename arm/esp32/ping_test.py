
# this is to test the ping sensor
# 
import time
from machine import Pin 
from machine import time_pulse_us

# 
#
def main():
    # initiate constants
    #
    SENSOR_PIN = 27
    SOUND_SPEED = 340   # m/s    

    # make the signal pin as output to send the pulse
    #
    sensor = Pin(SENSOR_PIN, Pin.OUT)
    
    # clear turn off the pin to clear
    # FIXME: change the clear time
    #
    sensor.value(0)
    time.sleep_us(5) 
    
    # send a pulse 
    #
    sensor.value(1)
    time.sleep_us(2)

    
    # HOLDOFF
    #
    sensor.value(0)
    time.sleep_us(750)

    
    # make the signal pin as input to re
    #
    sensor = Pin(SENSOR_PIN, Pin.IN)
    
    pulse_time = time_pulse_us(sensor, 1)
    
    
    dist_mm = pulse_time * 100 // 582
    dist_inches = dist_mm * 0.0393701 
    
    time.sleep_ms(65)
    
    print("distance {} inches".format(dist_inches))



    

#
#
if __name__ == "__main__":
    main()