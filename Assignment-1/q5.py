# If it costs 1600 rs. to fence a rectangular park of length 20 m at the rate of 25 rs. per m², find the breadth of the park and its perimeter. Also, find the area of the field.

total_cost = 1600
rate_per_meter_sq = 25

perimeter_park = total_cost / rate_per_meter_sq
print("Perimeter of the park: ",perimeter_park)

length_park = 20
breadth_park = (perimeter_park / 2) - length_park
print("Breadth of the park: ", breadth_park)

area_park = length_park*breadth_park
print("Area of the park: ",area_park)

