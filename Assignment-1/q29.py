# 29. How many square tiles of side 10 cm will be required to tile a floor measuring 800 cm by 900 cm?

side_tile = 10
area_tile = side_tile * side_tile

floor_dimension1 = 800
floor_dimension2 = 900
area_floor = floor_dimension1 * floor_dimension2

no_of_tiles_req = area_floor/ area_tile
print("No of tiles required: ", no_of_tiles_req)