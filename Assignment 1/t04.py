"""
-------------------------------------------------------
Assignment 1 Task 4

Given the cost of and quantity of pizza slices, the program calculates the total cost
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      169027577
Email:   chis7577@mylaurier.ca
__updated__ = "2022-09-26"
-------------------------------------------------------
"""
# Imports

# Constants
    
cost = float(input("Cost of one pizza slice: $")) #cost per pizza slice
num_slices = int(input("Number of pizza slices: ")) #number of pizza slices

total_cost = (cost * num_slices) #calculation for total cost of slices

print(f"Total cost of {num_slices} pizza slices: $ {total_cost}")
