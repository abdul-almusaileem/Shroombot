
#
#
import time
import sys
import os

# import other files
#
CWD = os.getcwd()
sys.path.append(CWD+'/vision/detection/')
sys.path.append(CWD+'/arm/rpi/')

from mushroom_finder import detect_mushroom
from move_arm import move_arm

#
#
def main():
  
    try:
        # ip of esp and port for the socket connection
        #
        ESP_IP = "10.42.0.102"
        PORT = 5001
        CAMERA_X_SHIFT = 15.95
        CAMERA_Y_SHIFT = 2.61

        SHROOMS = []
        
        SHROOMS = detect_mushroom()
        print(SHROOMS)
        
        for shroom_posission in SHROOMS:
                x = float(shroom_posission[0])
                y = float(shroom_posission[1])
                x = x - CAMERA_X_SHIFT
                y = y - CAMERA_Y_SHIFT
                flag = move_arm(x=x, y=y, ip=ESP_IP, port=PORT)
                
    except KeyboardInterrupt as err:
        sys.exit()

        

if __name__ == "__main__":
    main()