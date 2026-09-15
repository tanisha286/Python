# 19. A cube with an edge of 7 cm and a cuboid measuring 7 cm × 4 cm × 8 am are kept on a table. Which shape has more volume?

side_cube = 7
volume_of_cube = side_cube ** 3

length_cuboid = 7
breadth_cuboid = 4
height_cuboid = 8

volume_of_cuboid = length_cuboid* breadth_cuboid* height_cuboid

if volume_of_cube > volume_of_cuboid:
  print("Cube has more volume")
elif volume_of_cuboid > volume_of_cube:
  print("Cuboid has more volume")
else:
  print("Both have the same volume")
