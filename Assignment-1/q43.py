# 43. Find the cost of polishing the base of a cone whose height is 4cm and slant height 5 cm at the rate of 10 rs. Per sq. cm

height = 4
slant_height = 5
rate = 10

radius = (slant_height ** 2 - height ** 2) ** 0.5

base_area = 3.14 * radius ** 2

cost = base_area * rate

print(cost)