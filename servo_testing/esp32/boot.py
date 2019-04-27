from machine import Pin
from time import sleep

def custom_boot():
    
    p0 = Pin(22, Pin.OUT)

    for i in range(1, 10):
        p0.on()
        sleep(1)
        p0.off()
        sleep(1)

custom_boot()
