
# this is a class represents the arm
#

from servo import Servo as servo


# class as a struct for joint names
#
class Joints():
    base = 0
    lower_elbow = 1
    higher_elbow = 2
    mid_arm = 3
    wrist = 4
    
    
    

class Arm():

    # initiate used variables
    #
    
    # connections
    #
    TX_PIN = 16
    RX_PIN = 17
    
    # objects
    #
    CONNECTION = servo(TX_PIN, RX_PIN)
    JOINTS = Joints()

    # TODO: maybe add a dict {joint: angle} ?
    #

    #
    #
    def __init__(self):
        pass
        #self.IDLE()
    
    
    #
    #
    def IDLE(self):
        pass
        print("put the arm into idle position...")
        self.CONNECTION.center(self.JOINTS.lower_elbow)
        self.CONNECTION.center(self.JOINTS.wrist)
        self.CONNECTION.move(self.JOINTS.higher_elbow, 150, 200)
        self.CONNECTION.move(self.JOINTS.mid_arm, 900, 200)
        
    
    #
    #
    def IK(self, x, y, z):
        pass
        print("math ? or maybe just move to")
 
    
    def pick(self):
        pass
    
    def drop(self):
        pass    
    
    
    def demo(self):
        pass 
        self.CONNECTION.move(self.JOINTS.wrist, 100, 100)
    
    