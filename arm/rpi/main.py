
import sys
from move_arm import move_arm
# 
#
def main():
  
    while True:
        try:
            # take the coordinate of the targer
            #
            x_input = float(input("X: "))
            y_input = float(input("Y: "))

            # ip of esp and port for the socket connection
            #
            ip = "10.42.0.102"
            port = 5001
            
            # 
            #
            move_arm(x = x_input, y = y_input, ip = ip, port = port)
        
        except KeyboardInterrupt:
            sys.exit()
        except ValueError:
            print("please enter a number")
            continue 


#
#
if __name__ == "__main__":
    main()
