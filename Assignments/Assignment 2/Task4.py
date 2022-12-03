"""
-------------------------------------------------------
Assignment 2 Task 4
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      *********
Email:   *********
__updated__ = "2022-10-03"
-------------------------------------------------------
"""
# Imports

# Constants

pieces = int(input("Number of pieces of cake: "))
party_goers = int(input("Number of party-goers: "))

cake = pieces // party_goers
left_overs = pieces % party_goers

print(f"\nEach party-goer receives {cake} pieces of cake")
print(f"Pieces of cake that won’t be distributed: {left_overs}")
