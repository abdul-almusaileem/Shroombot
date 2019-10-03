
from ikpy.chain import Chain
from ikpy.link import OriginLink, URDFLink
from ikpy import plot_utils
import numpy as np
import matplotlib.pyplot as plt
from time import sleep
import math


SCALER = 10

# TODO: change translation vectors to vars of lengths
# TODO: change the translation vectors to be not on one axis because that
# TODO: ... makes the rotation from X-axis with no rotation on others ?
#
arm = Chain(name="arm", links= [
    # base servo
    #
    URDFLink(
        name = "base servo",
        translation_vector = [0, 0, 0], # location 
        orientation = [0, 0, 0],
        rotation = [0, 0, 1],
        bounds = (math.radians(0), math.radians(192))
        # bounds = (math.radians(-192), math.radians(0))
        ),
    
    URDFLink(
        name = "elbow low",
        translation_vector = [0, 0, 0.85 * SCALER], # location
        orientation = [0, 0, 0],
        rotation = [0, 1, 0],
        bounds = (math.radians(36), math.radians(144))
        # bounds = (math.radians(-144), math.radians(36))

        ),
    
    URDFLink(
        name = "elbow hight",
        translation_vector = [0.25 * SCALER, 0, 0], # location
        orientation = [0, 0, 0],
        rotation = [0, 1, 0],
        bounds = (math.radians(0), math.radians(28)) # FIXME: CHECK BOUNDS
        # bounds = (math.radians(-28), math.radians(0))

        ),

    URDFLink(
        name = "middle",
        translation_vector = [0.9 * SCALER, 0, 0], # location
        orientation = [0, 0, 0],
        rotation = [0, 1, 0],
        bounds = (math.radians(144), math.radians(240))
        # bounds = (math.radians(-144), math.radians(240))
        
        ),

    URDFLink(
        name = "wrist",
        translation_vector = [0.55 * SCALER, 0, 0], # location
        orientation = [0, 0, 0],
        rotation = [0, 1, 0],
        bounds = (math.radians(120), math.radians(216))
        # bounds = (math.radians(-120), math.radians(216))
        )
     
    # ,URDFLink(
    #     name = "end effector",
    #     translation_vector = [0.1*10, 0, 0], # location
    #     orientation = [0, 0, 0],
    #     rotation = [0, 1, 0])
])

# declate the axis 
#
ax = plot_utils.init_3d_figure()

#

# the target point between -1 ~ 1 in all axis 
# create the 
#
x = .0 * SCALER
y = 3. * SCALER
z = .0 * SCALER
target_vector = [x, y, z]
target_frame = np.eye(4)
target_frame[:3, 3] = target_vector


angles = arm.inverse_kinematics(target_frame)
for (i, angle) in enumerate(angles):
    angles[i] = math.degrees(angle) 
    if (angles[i] > 360 ):
        angles[i] = angles[i] % 360
        
    print("angle({}) = {} deg, {} pos".format(i, angles[i], int(angles[i]/0.24)))


arm.plot(arm.inverse_kinematics(target_frame), ax, target=target_vector)


# sleep(2)
# print("showing moving arm")

# new_ax = plot_utils.init_3d_figure()




# new_target_vector = [x, y, 0]
# target_frame[:3, 3] = new_target_vector
# copy target vector 
#
tmp_target_vector = target_vector

# new axis for the movement


# this loop is to see the motion when moving down to pick the mushrooms
# when implementing just switch z from VALUE to zero 
#
# for i in range(int(tmp_target_vector[2]*10+1)):
#     print("z = {}".format(tmp_target_vector[2]))
#     print("The angles of each joints are : ", arm.inverse_kinematics(target_frame))
#     arm.plot(arm.inverse_kinematics(target_frame), new_ax, target=target_frame)
#     tmp_target_vector[2] -= 0.1
#     target_frame[:3, 3] = tmp_target_vector
#     print("-" * 100)



    


# plot 
#
# plt.xlim(-SCALER, SCALER)
# plt.ylim(-SCALER, SCALER)
plt.show()

real_frame = arm.forward_kinematics(arm.inverse_kinematics(target_frame))
print("Computed position vector : %s, original position vector : %s" % (real_frame[:3, 3], target_frame[:3, 3]))
