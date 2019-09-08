from math import *
from numpy import rad2deg

# length of each segments 
#
a1 = 13
a2 = 3

# the desired point 
# 
x = int(input("enter x: "))
y = int(input("enter y: "))


#
#
r = sqrt(x**2 + y**2)

phi1 = atan(y/x)
phi2 = acos((a2**2 - a1**2 - r**2)/ (-2 * a1 * r))
theta1 = phi1 -  phi2

theta1_deg = rad2deg(theta1)

#
#
phi3 = acos((r**2 - a2**2 - a1**2) / (-2 * a2 * a1))

theta2 = 180 - rad2deg(phi3)
theta2_deg = rad2deg(theta2)

print("theta1: {}".format(theta1_deg))
print("theta2: {}".format(theta2_deg)) 
