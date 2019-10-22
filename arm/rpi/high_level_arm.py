
# this is a high level function that takes a pint (X, Y, Z)
# it then coputes the inverse kinematics to get the angle of each joint on the 
# arm those angle are then sent to the esp32 via socket
#
# TODO: write module to load arm from to be clean 
# TODO: look into websockets vs sockets ?
#

import sys
import numpy as np
import math
import time

# 
#
def main():
   try:
    while True:
        # take the coordinate of the targer
        #
        x_input = float(input("X: "))
        y_input = float(input("Y: "))
        # z_input = float(input("Z: "))

        # ip and port for the socket connection
        #
        ip = "172.20.10.6"
        port = 5001
        
        # 
        #
        arm_high_level(x = x_input, y = y_input, ip = ip, port = port)
   except KeyboardInterrupt:
       sys.exit()
    

# this is the function to be coppied to the Rpi
# TODO: make a debug flag to have all prints
#
def arm_high_level(x, y, ip, port):
    # load modules 
    #
    import arm_chain
    from send_angles_sockets import send_angles
    from recv_dist import recv_z
    from get_angles import compute_angles

    

    # initiate the arm chain object
    #
    arm = arm_chain.arm
    
    # compute the target frame (homogeneous matrix) where the specified point is 
    # TODO: Z will be hard coded as high value 
    #
    target_vector = [x, y, 10.5]
    target_frame = np.eye(4)
    target_frame[:3, 3] = target_vector

    #
    #
    angles = compute_angles(arm, target_frame)
    
    # send the angles to the esp32 via socket
    #
    send_angles(angles=angles, ip=ip, port=port)
    
    # wait some time ? 
    #
    #time.sleep(5)
    # rcv z from esp
    # TODO: check if u have z or not 
    #
    z_received = recv_z(host="172.20.10.3", port=5002)
    
    print("this is the new z value {}".format(z_received))
    
    # recompute the angles with the new z
    #
    target_vector = [x, y, z_received]
    target_frame = np.eye(4)
    target_frame[:3, 3] = target_vector
    angles = compute_angles(arm, target_frame)


    # send the angles to the esp32 via socket
    #
    send_angles(angles=angles, ip=ip, port=port)
    
    

    


if __name__ == "__main__":
    main()