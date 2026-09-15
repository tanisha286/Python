# 23. Find the number of cubical boxes of cubical side 3 cm which can be accommodated in carton of dimensions 15 cm × 9 cm × 12 cm.

side_cubical_boxes = 3
volume_cubical_boxes = side_cubical_boxes ** 3

carton_dimension1 = 15
carton_dimension2 = 9
carton_dimension3 = 12
volume_carton = carton_dimension1 * carton_dimension2* carton_dimension3

no_of_cubical_box = volume_carton /  volume_cubical_boxes 
print("No of cubical boxes required: ", no_of_cubical_box)