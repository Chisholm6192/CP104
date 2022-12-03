"""
-------------------------------------------------------
Assignment 4 Task 1
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      *********
Email:   *********
__updated__ = "2022-10-26"
-------------------------------------------------------
"""

day = day_of_week(7)
print(day)

def day_of_week(day_number):
    """
    -------------------------------------------------------
    Picks the name of the day based on the number given by user
    Use: day = day_of_week(day_number)
    -------------------------------------------------------
    Parameters:
        day_number - an integer (int > 0)
    Returns:
        day - the name of the day (str)
    ------------------------------------------------------
    """
    if day_number >= 1 and day_number <= 7:
        if day_number == 1:
            day = "Monday"
            
        elif day_number == 2:
            day = "Tuesday"
            
        elif day_number == 3:
            day = "Wednesday"
            
        elif day_number == 4:
            day = "Thursday"
            
        elif day_number == 5:
            day = "Friday"
            
        elif day_number == 6:
            day = "Saturday"
            
        elif day_number == 7:
            day = "Sunday"
        
    else:
        day = "Error"
        
    return day
