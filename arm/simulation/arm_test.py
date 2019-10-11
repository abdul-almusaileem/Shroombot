
from ikpy.chain import Chain
from ikpy.link import OriginLink, URDFLink
from ikpy import plot_utils
import numpy as np
import matplotlib.pyplot as plt
from time import sleep
import math


SCALER = 10

# TODO: check length of each link could be wrong
#
arm = Chain(name="arm", links= [
    # base servo
    #
    URDFLink(
        name = "base servo",
        translation_vector = [0, 0, 0], # location 
        orientation = [ 0, 0, 0],
        rotation = [0, 0, 1],
        # bounds = (math.radians(130), math.radians(240))
        # bounds = (math.radians(-192), math.radians(0))
        bounds = (math.radians(0), math.radians(240))

        ),
    
    URDFLink(
        name = "elbow low",
        translation_vector = [0, 0, 0.95 * SCALER], # location
        orientation = [0, 0, 0],
        rotation = [0, 1, 0],
        # bounds = (math.radians(36), math.radians(144))
        # bounds = (math.radians(-144), math.radians(36))
        bounds = (math.radians(0), math.radians(240))


        ),
    
    URDFLink(
        name = "elbow hight",
        translation_vector = [0, 0, 0.25 * SCALER], # location
        orientation = [0, 0, math.pi],
        rotation = [0, 1, 0],
        bounds = (math.radians(0), math.radians(144)) 
        # bounds = (math.radians(-144), math.radians(36))
        # bounds = (math.radians(0), math.radians(240))
        

        ),

    URDFLink(
        name = "middle",
        translation_vector = [0.9 * SCALER, 0, 0], # location
        orientation = [0, 0, -math.pi],
        rotation = [0, 1, 0],
        # maybe set the lower bound to 120 so that it doesn't point up
        #
        bounds = (math.radians(120), math.radians(240)) 
        # bounds = (math.radians(-240), math.radians(120))
        
        ),

    URDFLink(
        name = "wrist",
        translation_vector = [0.55 * SCALER, 0, 0], # location
        orientation = [0, 0, 0],
        rotation = [0, 1, 0],
        bounds = (math.radians(0), math.radians(240))
        # bounds = (math.radians(-120), math.radians(216))
        )
     
    # ,URDFLink(
    #     name = "end effector",
    #     translation_vector = [0.1 * SCALER, 0, 0], # location
    #     orientation = [0, 0, 0],
    #     rotation = [0, 1, 0])
])

# declate the axis 
#
ax = plot_utils.init_3d_figure()

#

# take the coordinate of the targer
#
x_input = float(input("X: "))
y_input = float(input("Y: "))
z_input = float(input("Z: "))

# initiate the target vector and the target frame
#
x = x_input #* SCALER
y = y_input #* SCALER
z = z_input #* SCALER
target_vector = [x, y, z]
target_frame = np.eye(4)
target_frame[:3, 3] = target_vector


angles = arm.inverse_kinematics(target_frame)
for (i, angle) in enumerate(angles):
    angles[i] = math.degrees(angle) 
    
    # brandon logic to map things one at a time by changing maps
    #
    if (i == 0):
        angles[i] = 0 + angles[i]   
    elif (i == 1): 
        angles[i] = 0 + angles[i]          
    elif (i == 2):
        angles[i] = round(angles[i])
        angles[i] = 0 + abs(angles[i]) 
    elif (i == 3):
        angles[i] = 0 + angles[i]          

    print("angle({}) = {} deg, {} pos".format(i, angles[i], int(angles[i]/0.24)))


arm.plot(arm.inverse_kinematics(target_frame), ax, target=target_vector)

# check if reached !
#
real_frame = arm.forward_kinematics(arm.inverse_kinematics(target_frame))
print("Computed position vector : %s, original position vector : %s" % (real_frame[:3, 3], target_frame[:3, 3]))

    

print("-" * 80)

new_target_vector = [x, y, 0]
new_target_frame = np.eye(4)
new_target_frame[:3, 3] = new_target_vector
# new_ax = plot_utils.init_3d_figure()

angles = arm.inverse_kinematics(new_target_frame)
for (i, angle) in enumerate(angles):
    angles[i] = math.degrees(angle) 
    
    # brandon logic to map things one at a time by changing maps
    #
    if (i == 0):
        angles[i] = 0 + angles[i]   
    elif (i == 1): 
        angles[i] = 0 + angles[i]          
    elif (i == 2):
        angles[i] = round(angles[i])
        angles[i] = 0 + abs(angles[i]) 
    elif (i == 3):
        angles[i] = 0 + angles[i]          
            
    
    print("angle({}) = {} deg, {} pos".format(i, angles[i], int(angles[i]/0.24)))

        
#arm.plot(arm.inverse_kinematics(new_target_frame), ax, target=new_target_frame)
#real_frame = arm.forward_kinematics(arm.inverse_kinematics(new_target_frame))
print("Computed position vector : %s, original position vector : %s" % (real_frame[:3, 3], new_target_frame[:3, 3]))



# plot 
#
# plt.xlim(-SCALER, SCALER)
# plt.ylim(-SCALER, SCALER)
plt.show()
