
from ikpy.chain import Chain
from ikpy.link import OriginLink, URDFLink
from ikpy import plot_utils
import numpy as np
import matplotlib.pyplot as plt
from time import sleep


# TODO: change translation vectors to vars of lengths
#
arm = Chain(name="arm", links= [
    # base servo
    #
    URDFLink(
        name = "base servo",
        translation_vector = [0, 0, 0], # location 
        orientation = [0, 0, 0],
        rotation = [0, 0, 1]),
    
    URDFLink(
        name = "elbow low",
        translation_vector = [0, 0, 0.6], # location
        orientation = [0, 0, 0],
        rotation = [0, 1, 0]),
    
    URDFLink(
        name = "elbow hight",
        translation_vector = [0.1, 0, 0], # location
        orientation = [0, 0, 0],
        rotation = [0, 1, 0]),

    URDFLink(
        name = "middle",
        translation_vector = [0.6, 0, 0], # location
        orientation = [0, 0, 0],
        rotation = [0, 1, 0]),

    URDFLink(
        name = "wrist",
        translation_vector = [0.25, 0, 0], # location
        orientation = [0, 0, 0],
        rotation = [0, 1, 0])
])

# declate the axis 
#
ax = plot_utils.init_3d_figure()

#

# the target point between -1 ~ 1 in all axis 
# create the 
#
target_vector = [.2, .70, .4]
target_frame = np.eye(4)
target_frame[:3, 3] = target_vector


# print(arm)
# print("The angles of each joints are : ", arm.inverse_kinematics(target_frame))


arm.plot(arm.inverse_kinematics(target_frame), ax, target=target_vector)
# plt.xlim(-1, 1)
# plt.ylim(-1, 1)
# plt.show()


# sleep(2)
# print("showing moving arm")

# new_target_vector = [.5, .5, 0]
# target_frame[:3, 3] = new_target_vector
# arm.plot(arm.inverse_kinematics(target_frame), ax, target= new_target_vector)
# plt.xlim(-1, 1)
# plt.ylim(-1, 1)
# plt.show()

# copy target vector 
#
tmp_target_vector = target_vector

# new axis for the movement
#
new_ax = plot_utils.init_3d_figure()

# this loop is to see the motion when moving down to pick the mushrooms
# when implementing just switch z from VALUE to zero 
#
for i in range(int(tmp_target_vector[2]*10+1)):
    print("z = {}".format(tmp_target_vector[2]))
    print("The angles of each joints are : ", arm.inverse_kinematics(target_frame))
    arm.plot(arm.inverse_kinematics(target_frame), new_ax, target=target_frame)
    tmp_target_vector[2] -= 0.1
    target_frame[:3, 3] = tmp_target_vector
    print("-" * 100)

    


# plot 
#
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.show()

real_frame = arm.forward_kinematics(arm.inverse_kinematics(target_frame))
print("Computed position vector : %s, original position vector : %s" % (real_frame[:3, 3], target_frame[:3, 3]))
