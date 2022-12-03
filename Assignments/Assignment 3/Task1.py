"""
-------------------------------------------------------
Assignment 3 Task 1
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      *********
Email:   *********
__updated__ = "2022-10-13"
-------------------------------------------------------
"""
# Constants
ACRE = 43560

square_footage = float(input("Square footage: "))
acres = feet_to_acres(square_footage)

print(f"\n{acres:.02f} acres is equivalent to {square_footage:,.02f} square feet")

def feet_to_acres(square_footage):
    """
    -------------------------------------------------------
    Converts square footage to acres.
    Use: acres = feet_to_acres(square_footage)
    -------------------------------------------------------
    Parameters:
        square_footage - area in square feet (float >= 0)
    Returns:
        acres - square_footage in acres (float)
    ------------------------------------------------------
    """
    acres = square_footage / ACRE
    
    return acres
