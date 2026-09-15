# 21. A brick measures 15 cm in length, 8 cm in breadth and 5 cm in height. How many bricks will be used to make a wall of length 15 m, breadth 10 m and height 8 metres?

length_brick = 15
breadth_brick = 8
height_brick = 5
volume_of_brick = length_brick* breadth_brick* height_brick

length_wall = 15 * 100 # converting into cm
breadth_wall = 10 * 100
height_wall = 8 * 100
volume_of_wall = length_wall* breadth_wall * height_wall

no_of_bricks_req = volume_of_wall/ volume_of_brick
print("The no of bricks required: ", no_of_bricks_req)