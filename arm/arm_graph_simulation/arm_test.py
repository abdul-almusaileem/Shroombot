
from ikpy.chain import Chain
from ikpy.link import OriginLink, URDFLink
from ikpy import plot_utils
import numpy as np
import matplotlib.pyplot as plt


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

# the target point between -1 ~ 1 in all axis 
# 
target_vector = [.5, .25, .30]
target_frame = np.eye(4)
target_frame[:3, 3] = target_vector


print(arm)
print("The angles of each joints are : ", arm.inverse_kinematics(target_frame))

real_frame = arm.forward_kinematics(arm.inverse_kinematics(target_frame))
print("Computed position vector : %s, original position vector : %s" % (real_frame[:3, 3], target_frame[:3, 3]))

ax = plot_utils.init_3d_figure()
arm.plot(arm.inverse_kinematics(target_frame), ax, target=target_vector)
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.show()