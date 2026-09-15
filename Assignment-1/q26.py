# 26. How many bricks will be required to lay a path 120 m long and 2.4 m breadth if a brick is 24 cm long and 15 cm wide?

length = 120
breadth = 2.4

area = length * breadth

area = area * 10000 #m sq to cm sq

brick_length = 24
brick_width = 15

brick_area = brick_length * brick_width
no_of_bricks = area  / brick_area

print("Number of bricks: ", no_of_bricks)
