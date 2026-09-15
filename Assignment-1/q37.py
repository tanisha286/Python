# 37. The surface of the cylinder is 149 cm². The cylinder height is 6 cm. What is the diameter of this cylinder?

import math 

surface_area = 149
height = 6

a = 2 * math.pi
b = 2 * math.pi * height 
c = -surface_area

radius = (-b + math.sqrt(b ** 2 - 4 * a * c)) / ( 2 * a)
diameter = 2 * radius

print("Diameter: ",diameter)