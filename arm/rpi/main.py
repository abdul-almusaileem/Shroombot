
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
        FILE_NAME = "shroom_coordinates.txt"
        SHROOMS = []
        
        # take the coordinate of the targer
        #
        # x_input = float(input("X: "))
        # y_input = float(input("Y: "))
            
        # move the arm to the given coordinate
        #
        # move_arm(x = x_input, y = y_input, ip = ESP_IP, port = PORT)

        # read the lines from the file
        # remove '\n' from each line then split the into two array
        # convert the coordinates into floats
        # pass the coordinates to the arm  
        #
        with open(FILE_NAME, "r") as file:
            SHROOMS = file.readlines()
            
            for shroom_posission in SHROOMS:
                shroom_posission = shroom_posission.rstrip()
                shroom_posission = shroom_posission.split(" ")

                x = float(shroom_posission[0])
                y = float(shroom_posission[1])
                flag = move_arm(x=x, y=y, ip=ESP_IP, port=PORT)
                
                time.sleep(1)
            
    
    except KeyboardInterrupt:
        sys.exit()

      

#
#
if __name__ == "__main__":
    main()
