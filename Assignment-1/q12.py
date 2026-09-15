# 12. Find the area of a right angled triangle whose hypotenuse is 13 cm and one of its sides containing the right angle is 12 cm. Find the length of the other side.

import math

hypotenuse = 13
side = 12
#pythagoras theorem
other_side = math.sqrt(hypotenuse **2 - side ** 2)

area = 1/2 *  side * other_side

print("The area is: ", area)