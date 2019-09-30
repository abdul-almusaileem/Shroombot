

from ikpy.chain import Chain
from ikpy.link import OriginLink, URDFLink
from ikpy import plot_utils
import numpy as np

my_chain = Chain(name='left_arm', links=[
    # OriginLink(),
    URDFLink(
      name="shoulder",
      translation_vector=[0, 0, 0],
      orientation=[0, 1.57, 0],
      rotation=[0, 0, 1],
    ),
    URDFLink(
      name="elbow",
      translation_vector=[.5, .2, 0],
      orientation=[0, 0, 0],
      rotation=[0, 1, 0],
    ),
    URDFLink(
      name="wrist",
      translation_vector=[0.5, 0, 0],
      orientation=[0, 0, 0],
      rotation=[0, 0, 1],
    )
])

target_vector = [.5, -0.75, 0]
target_frame = np.eye(4)
target_frame[:3, 3] = target_vector

print(my_chain)

print("The angles of each joints are : ", my_chain.inverse_kinematics(target_frame))

real_frame = my_chain.forward_kinematics(my_chain.inverse_kinematics(target_frame))
print("Computed position vector : %s, original position vector : %s" % (real_frame[:3, 3], target_frame[:3, 3]))

import matplotlib.pyplot as plt
ax = plot_utils.init_3d_figure()
my_chain.plot(my_chain.inverse_kinematics(target_frame), ax, target=target_vector)
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.show()