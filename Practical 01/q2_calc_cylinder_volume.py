# Filename: q2_calc_cylinder_volume.py
# Author: Chia Xiang Rong
# Date created: 21/1/2013
# Date modified: 22/1/2013
# Description: Computation of the value of a cylinder given
# its radius and length

#Find radius
radius = float(input("Enter radius of cylinder: "))

#Find length
length = float(input("Enter length of cylinder: "))

#Compute volume
from math import pi
volume = radius * radius * pi * length

#Display volume of cylinder
print ("Volume of cylinder (cm^3) = {0}".format(volume))
