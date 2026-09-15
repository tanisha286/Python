# 4. Find the cost of tiling a rectangular plot of land 300 m long and 150 m wide at the rate of $6 per hundred square m. 

length_plot = 300
width_plot = 150
rate = 6

area = length_plot* width_plot
sections = area / 100

cost = rate * sections
print("Cost for tiling the plot: ", cost)
