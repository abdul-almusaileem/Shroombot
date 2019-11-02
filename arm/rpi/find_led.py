
# this is a simple script to find which gpio is the led using
#
import RPi.GPIO as GPIO 
from time import sleep 

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

for i in range(1, 26):
    print("GPI: {}".format(i))
    GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW)
    GPIO.output(8, GPIO.HIGH)
    sleep(1)
    GPIO.output(8, GPIO.LOW) 
    sleep(1)