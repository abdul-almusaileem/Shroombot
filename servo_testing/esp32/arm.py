
# this is a class represents the arm
#

from servo import Servo as servo
from time import sleep



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
    #    pass
        #sleep(1)
        self.IDLE()
    
    
    #
    #
    def IDLE(self):
        pass
        print("put the arm into idle position...")
        sleep(0.5)
        self.CONNECTION.center(self.JOINTS.lower_elbow)
        sleep(0.5)
        self.CONNECTION.move(self.JOINTS.higher_elbow, 150, 500)
        sleep(0.5)
        self.CONNECTION.move(self.JOINTS.mid_arm, 900, 500)
        sleep(0.5)
        self.CONNECTION.center(self.JOINTS.wrist)

        
    
    #
    #
    def IK(self, x, y, z):
        pass
        print("math ? or maybe just move to")
 

    # this method would send a signal to the actuator to pick the mushroom
    # this method also would read from either a pressure or a ping sensor
    # to determine whether a mushroom was picked or not
    #
    def pick(self):
        pass

    # this method would rotate the arm to the location of the basket
    # then place the mushroom there 
    #
    def drop(self):
        pass    
    

    # this method was for demo purposes in the first preitntaion
    #
    def demo(self):
        pass 
        self.CONNECTION.move(self.JOINTS.higher_elbow, 0, 500)
        self.CONNECTION.move(self.JOINTS.mid_arm, 600,  500)
        self.CONNECTION.move(self.JOINTS.wrist, 700, 500)
        sleep(2)
        
        self.IDLE()
        sleep(2)

        self.CONNECTION.move(self.JOINTS.higher_elbow, 300, 500)
        self.CONNECTION.move(self.JOINTS.mid_arm, 500,  500)
        self.CONNECTION.move(self.JOINTS.wrist, 500, 500)
        sleep(1)
        
        self.IDLE()
        sleep(2)
        
        self.CONNECTION.move(self.JOINTS.lower_elbow, 350, 500)
        self.CONNECTION.move(self.JOINTS.higher_elbow, 150, 500)
        self.CONNECTION.move(self.JOINTS.mid_arm, 830,  500)
        self.CONNECTION.move(self.JOINTS.wrist, 550, 500)
        sleep(2)
        
        self.IDLE()  
        sleep(2)

        
        
    
