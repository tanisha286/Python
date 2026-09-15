# 33. A rectangular garden has dimensions of 30 m by 20 m and is divided in to 4 parts by two pathways that run perpendicular from its sides. One pathway has a width of 3 m and the other, 4 m. Calculate the total usable area of the garden.

length = 30
breadth = 20

garden_area = length * breadth

path1 = length * 3
path2 = breadth * 4

overlap = 3*4
pathway_area = path1 + path2 - overlap

usable_area = garden_area - pathway_area
print("Usable area: ", usable_area)