"""
-------------------------------------------------------
Assignment 2 Task 5
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      *********
Email:   *********
__updated__ = "2022-10-03"
-------------------------------------------------------
"""
# Imports

# Constants

length = float(input("Foundation length (m): ")) #length of foundation
width = float(input("Foundation width (m): ")) #width of foundation
height = float(input("Foundation height (m): ")) #height of foundation
wall_height = float(input("Wall height (m): ")) #height of wall

cost_concrete = float(input("Cost of concrete ($/m^3): ")) #cost of concrete in dollars per meter cubed
cost_bricks = float(input("Cost of bricks ($/m^2): ")) #cost of bricks in dollars per meter squared

concrete_need = length * width * height #concrete needed for foundation, volume
total_concrete_cost = concrete_need * cost_concrete

bricks_need = (2*(wall_height * length)) + (2*(wall_height * width)) #bricks needed for walls, 4 walls and its rectangular
total_brick_cost = bricks_need * cost_bricks

total_cost = total_concrete_cost + total_brick_cost

print(f"\nConcrete needed for foundation (m^3): {concrete_need:.02f}")
print(f"Cost of concrete: ${total_concrete_cost:.02f}")
print(f"Bricks needed for walls (m^2): {bricks_need:.02f}")
print(f"Cost of bricks: ${total_brick_cost:,.02f}")
print(f"Total cost: ${total_cost:,.02f}")
