# 30. How many tiles of length 5 cm and breadth 8 cm are needed to tile the floor of a bed room 200 cm long and 400 cm wide?

length_tile = 5
breadth_tile = 8
area_tile = length_tile* breadth_tile

length_floor = 200
width_floor = 400
area_floor = length_floor* width_floor

no_of_tiles = area_floor/ area_tile
print("No of tiles required : ", no_of_tiles)
