
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
    pass


# this is the function to be coppied to the Rpi
#
def arm_high_level(x, y, z):
    pass

    # load modules 
    #

    # initiate the arm chain object
    #
    
    
    # compute the target frame  
    #
    
    
    # check if x is negative ?
    # 
    #
    
    # inverse kinematics to get angles
    #
    
    # remap the coordinates for each servo using Brandon's lOgIc
    # TODO: find a way where to put the function maybe module called remap? 
    #
    
    
    # compare with original point
    #
    
    # send the angles to the esp32 via socket
    # TODO: change the function perameters to take the host and the ports too
    #
    
    


if __name__ == "__main__":
    pass