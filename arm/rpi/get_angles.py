

#
#
def compute_angles(arm, target_frame):
    import math
    from remap import remap

    
     # check if the X is negative then set the flag 
    # and take the abs value to get compute the base then reverse angle in remap
    #
    x =  0
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


    return angles 