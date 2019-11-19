
# this is a high level function that takes a pint (X, Y, Z)
# it then coputes the inverse kinematics to get the angle of each joint on the 
# arm those angle are then sent to the esp32 via socket
#
# load modules 
#
import sys   
import numpy as np
import time
import math
import netifaces as ni
import arm_chain
from send_angles_sockets import send_angles
from recv_dist import recv_dist
from get_angles import compute_angles
from angles_no_repl import no_repl
from threshold import threshold
# import socket
#import math

#
#
def move_arm(x, y, ip, port):


    # get the local ip address of the machine running the script
    #
    if('en1' in ni.interfaces()):
        local_ip = ni.ifaddresses('en1')[ni.AF_INET][0]['addr']
    else:
        local_ip = ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']
        
    print("ip is {}".format(local_ip))

    # initiate the arm chain object
    #
    arm = arm_chain.arm
    
    Z_HIGH = 10.5
    
    # compute the target frame (homogeneous matrix) where the specified point is 
    #
    target_vector = [x, y, Z_HIGH]
    target_frame = np.eye(4)
    target_frame[:3, 3] = target_vector

    # compute the required angles to get to the target vector
    #
    angles = compute_angles(arm, target_frame)

    # uncomment to repl
    #
    # angles = no_repl()
    
    # compare where the end effector is with where the specified point is
    # 
    real_frame = arm.forward_kinematics(arm.inverse_kinematics(target_frame))
    print("Computed position vector : %s, original position vector : %s"\
         % (real_frame[:3, 3], target_frame[:3, 3]))

    
    # send the angles to the esp32 via socket
    #
    send_angles(angles=angles, ip=ip, port=port)
    
    # wait some time ? 
    #
    time.sleep(1)
    
    # rcv distance from esp
    #
    dist = recv_dist(host=local_ip, port=6666)
    
    # compute the z value from current hight
    # then add 0.5 inches to give space
    #
    z = Z_HIGH - dist
    z = z + (-0.7)
    
    print("this is the new z value {}".format(z))
    

    # to fix the suction cup offset
    #
    try:
        theta = math.atan(y / x)
    except ZeroDivisionError as err:
        theta = 0
    hyp = math.sqrt(x**2 + y**2)
    shifted_hyp = hyp - 0.5
    
    shifted_x = shifted_hyp * math.cos(theta)
    shifted_y = shifted_hyp * math.sin(theta) 
    # recompute the angles with the new z
    #
    new_target_vector = [shifted_x, shifted_y, z]
    new_target_frame = np.eye(4)
    new_target_frame[:3, 3] = new_target_vector
    new_angles = compute_angles(arm, new_target_frame)
    
    # wait some time ? 
    #
    time.sleep(1)

    # compare where the end effector is with where the specified point is
    # 
    real_frame = arm.forward_kinematics(arm.inverse_kinematics(new_target_frame))
    print("Computed position vector : %s, original position vector : %s" \
        % (real_frame[:3, 3], new_target_frame[:3, 3]))


    new_coordinates = real_frame[:3, 3]
    WINDOW = 0.75
    flag = threshold(real=[x, y, z], computed=new_coordinates, window=WINDOW)
    
    # check if the new computed coordinates are within the desired threshold 
    #
    if (flag):


        # send the angles to the esp32 via socket
        #
        send_angles(angles=new_angles, ip=ip, port=port)
    
    else:
        # send old angles
        #
        send_angles(angles=angles, ip=ip, port=port)
        print("staying in old...")


    # TODO: find a way to know that the arm is now at drop!
    #
    time.sleep(15)

    return 1