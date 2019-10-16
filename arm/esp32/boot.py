from wifi_connect import connect
import config
from machine import Pin

def main():
    
    #
    #
    LED_PIN = 26
    led = Pin(LED_PIN, Pin.OUT)
    led.value(0)
    
    addr = None
    
    addr = connect(config.SSID, config.PASS)
    led.value(1)

if __name__ == '__main__':
    main()
