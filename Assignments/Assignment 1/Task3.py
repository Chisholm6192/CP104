"""
-------------------------------------------------------
Assignment 1 Task 3
Conversion of inches to meters
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      *********
Email:   *********
__updated__ = "2022-09-26"
-------------------------------------------------------
"""
# Imports
# Constants
M = 0.0254 #constant for number of inches in a meter

    
inches = int(input("Length in inches: ")) #input for inches

Meters = float(inches * M) #constant for conversion of inches to meters

print(f"Length in m: {Meters}")
