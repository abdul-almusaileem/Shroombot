
#
#
import time
import sys
from vision.detection.mushroom_finder import detect_mushroom
from arm.rpi.move_arm import move_arm


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

        SHROOMS_COORDINATES = []
        
        SHROOMS_COORDINATES = detect_mushroom()
        print(SHROOMS_COORDINATES)
    except KeyboardInterrupt as err:
        sys.exit()

        

if __name__ == "__main__":
    main()