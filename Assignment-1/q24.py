# 24. How many bricks each 25 cm long, 10 cm wide and 7.5 cm thick will be required for a wall 20 m long, 2 m high and 0.75 m thick? If bricks sell at $900 per thousand what will it cost to build the wall?

length_brick = 25
height_brick = 10
widt_brick = 7.5
volume_of_brick = length_brick* height_brick* widt_brick

length_wall = 20 * 100
height_wall = 2 * 100
width_wall = 0.75 * 100
volume_of_wall = length_wall* height_wall* width_wall

no_bricks_req = volume_of_wall / volume_of_brick
print("No of bricks required is: ", no_bricks_req)

cost_per_thousand = 900
cost_req = (no_bricks_req/1000) * cost_per_thousand

print("Total cost required to build the wall: ", cost_req)

