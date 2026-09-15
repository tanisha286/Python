# 11. The base and height of a triangle are in the ratio 8 : 5 and its area is 320 m². Find the height and base of the triangle.

import math

area = 320
x = math.sqrt((2 * area) / (8 * 5))

base = 8 * x
height = 5 * x

print("Height: ", height)
print("Base: ", base)