
# this is a class represents the arm
#

from servo import Servo as servo


# class as a struct for joint names
#
class Joints():
    self.base = 0
    self.lower_elbow = 1
    self.higher_elbow = 2
    self.mid_arm = 3
    self.wrist = 4
    
    
    

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
        self.IDLE()
    
    
    #
    #
    def IDLE(self):
        pass
        print("put the arm into idle position...")
    
    #
    #
    def IK(self, x, y, z):
        pass
        print("math ? or maybe just move to")
 
    def 
    
    def pick(self):
        pass
    
    def drop(self):
        pass    
    
    
    def demo(self)
        pass 
       self.CONNECTION.move(self.JOINTS.wrist, 100, 100)
    
    