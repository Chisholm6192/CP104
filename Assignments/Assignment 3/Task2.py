"""
-------------------------------------------------------
Assignment 3 Task 2
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      *********
Email:   *********
__updated__ = "2022-10-15"
-------------------------------------------------------
"""

width = float(input("Width (m): "))
length = float(input("Length (m): "))
speed = float(input("Speed (m^2/minute): "))
time = mow_lawn(width, length, speed)

print(f"\nMowing the lawn takes {time:.0f} minutes")

def mow_lawn(width, length, speed):
    """
    -------------------------------------------------------
    Determines how long it takes to mow a rectangular lawn.
    Use: time = mow_lawn(width, length, speed)
    -------------------------------------------------------
    Parameters:
        width - width of a lawn in metres (float > 0)
        length - length of a lawn in metres (float > 0)
        speed - square metres cut per minute (float > 0)
    Returns:
        time - time required to mow the lawn in minutes (float)
    ------------------------------------------------------
    """
    area = width * length #area calculation
    time = area / speed 
    return time
