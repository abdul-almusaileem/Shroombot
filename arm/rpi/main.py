
import sys
import time
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
        
        FILE_PATH = "shroom_coordinates.txt"
        SHROOMS = []
        
       
        # read the lines from the file
        # remove '\n' from each line then split the into two array
        # convert the coordinates into floats
        # pass the coordinates to the arm  
        #
        with open(FILE_PATH, "r") as file:
            SHROOMS = file.readlines()
            
            for shroom_posission in SHROOMS:
                shroom_posission = shroom_posission.rstrip()
                shroom_posission = shroom_posission.split(" ")

                x = float(shroom_posission[0])
                y = float(shroom_posission[1])
                x = x - CAMERA_X_SHIFT
                y = y - CAMERA_Y_SHIFT
                flag = move_arm(x=x, y=y, ip=ESP_IP, port=PORT)
                print("picked??")
            
    
    except KeyboardInterrupt:
        sys.exit()

      

#
#
if __name__ == "__main__":
    main()
