
# this is a high level function that takes a pint (X, Y, Z)
# it then coputes the inverse kinematics to get the angle of each joint on the 
# arm those angle are then sent to the esp32 via socket
#
# TODO: write module to load arm from to be clean 
# TODO: look into websockets vs sockets ?
#

# 
#
def main():
    # take the coordinate of the targer
    #
    x_input = float(input("X: "))
    y_input = float(input("Y: "))
    z_input = float(input("Z: "))

    # ip and port for the socket connection
    #
    ip = "172.20.10.6"
    port = 5001
    
    # 
    #
    arm_high_level(x = x_input, y = y_input, z = z_input, ip = ip, port = port)

    

# this is the function to be coppied to the Rpi
#
def arm_high_level(x, y, z, ip, port):
    # load modules 
    #
    import arm_chain
    from send_angles_sockets import send_angles
    from remap import remap
    import numpy as np
    import math
    

    # initiate the arm chain object
    #
    arm = arm_chain.arm
    
    
    
    # compute the target frame (homogeneous matrix) where the specified point is 
    #
    target_vector = [x, y, z]
    target_frame = np.eye(4)
    target_frame[:3, 3] = target_vector

    # check if the X is negative then set the flag 
    # and take the abs value to get compute the base then reverse angle in remap
    #
    if (x < 0):
        x = abs(x)
        negX_flag = 1
    else:
        negX_flag = 0
    
    # compute the inverse Kinematics and store the angles for each joint
    #
    angles = arm.inverse_kinematics(target_frame)
    
    # remap the coordinates for each servo using Brandon's lOgIc
    # convert the angle from radian to degrees
    # remap each angle using Brandon's LoGic 
    # print each angle in degrees and position for debugging
    #
    for (i, angle) in enumerate(angles):
        angles[i] = math.degrees(angle) 
        angles[i] = remap(angles=angles, id=i, negX_flag=negX_flag)
        print("angle({}) = {} deg, {} pos".format(i, angles[i], int(angles[i]/0.24)))

    # compare where the end effector is with where the specified point is
    # 
    real_frame = arm.forward_kinematics(arm.inverse_kinematics(target_frame))
    print("Computed position vector : %s, original position vector : %s" % (real_frame[:3, 3], target_frame[:3, 3]))


    # send the angles to the esp32 via socket
    #
    send_angles(angles=angles, ip=ip, port=port)
    
    


if __name__ == "__main__":
    main()