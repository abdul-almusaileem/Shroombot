
# this is a class represents the arm
#

from servo import Servo as servo
from time import sleep



# class as a struct for joint names
# bounds:
# B (0, 800),
# L (200, 600),
# H (0, 150),
# M (600, 1000),
# W (500, 900)
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
        self.CONNECTION.move(self.JOINTS.base, 600, 500)
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
    def moveJoints(self, angles=[]):
        pass
        print("given {} angles are {}".format(len(angles), angles))
        
        # if no angle was passed set to IDLE
        # 
        if len(angles) == 0:
            self.IDLE()
            return
        
        # send each joint the corresbonding angle
        # TODO: maybe make an array of joints or leave this be
        # 
        for (id,angle) in enumerate(angles):
            position = self.conv_angle(angle)
            self.CONNECTION.move(ID=id, position=position, time=500)
            sleep(0.5)
        return 1
            
    
    
    # this function converts angles to possitoins 
    # TODO: maybe move to main file not in the class
    #
    def conv_angle(self, angle):
        CONV = .240
        pos = angle / .240
        print("pos: {}".format(pos))
        return int(pos)
   

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
    

    # this method was for demo purposes in the first presintaion
    #
    def demo(self):
        pass 
        self.CONNECTION.move(self.JOINTS.higher_elbow, 0, 500)
        self.CONNECTION.move(self.JOINTS.mid_arm, 600,  500)
        self.CONNECTION.move(self.JOINTS.wrist, 700, 500)
        self.CONNECTION.move(self.JOINTS.base, 1000, 500)
        sleep(1)
        self.CONNECTION.move(self.JOINTS.base, 600, 500)
        sleep(1)
        
        self.IDLE()
        sleep(2)

        self.CONNECTION.move(self.JOINTS.higher_elbow, 300, 500)
        self.CONNECTION.move(self.JOINTS.mid_arm, 500,  500)
        self.CONNECTION.move(self.JOINTS.wrist, 500, 500)
        self.CONNECTION.move(self.JOINTS.base, 1000, 500)
        sleep(1)
        self.CONNECTION.move(self.JOINTS.base, 600, 500)
        sleep(1)
        
        self.IDLE()
        sleep(2)
        
        self.CONNECTION.move(self.JOINTS.lower_elbow, 350, 500)
        self.CONNECTION.move(self.JOINTS.higher_elbow, 150, 500)
        self.CONNECTION.move(self.JOINTS.mid_arm, 830,  500)
        self.CONNECTION.move(self.JOINTS.wrist, 550, 500)
        self.CONNECTION.move(self.JOINTS.base, 1000, 500)
        sleep(1)
        self.CONNECTION.move(self.JOINTS.base, 600, 500)
        sleep(1)
        
        self.IDLE()  
        sleep(2)

        
        
    
