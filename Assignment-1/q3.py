# 3. How many tiles whose length and breadth are 13 cm and 7 cm respectively are needed to cover a rectangular region whose length and breadth are 520 cm and 140 cm? 

length_tile = 13
breadth_tile = 7
area_tile = length_tile* breadth_tile

length_rectangle = 520
breadth_rectangle = 140
area_rectangle = length_rectangle* breadth_rectangle

no_of_tiles_req = area_rectangle / area_tile
print("Number of tiles required: ", no_of_tiles_req)