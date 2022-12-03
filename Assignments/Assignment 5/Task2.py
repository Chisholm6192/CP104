"""
-------------------------------------------------------
Assignment 5 Task 2
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      *********
Email:   *********
__updated__ = "2022-11-03"
-------------------------------------------------------
"""

calories = calories_burned(2, 3)



def calories_burned(per_minute, minutes):
    """
    -------------------------------------------------------
    Calculates the amount of calories burned at each interval of five minutes
    Use: calories = calories_burned(per_minute, minutes)
    -------------------------------------------------------
    Parameters:
        per_minute - the number of calories burned per minute (float >= 0)
        minutes - the total number of minutes on the treadmill (int >= 0)
    Returns: None
    ------------------------------------------------------
    """
    total_calories_burned = 0
    
    for i in range(5, minutes + 1, 5):
                
        total_calories_burned = per_minute * i
        
        print(f' {i:2}: {total_calories_burned:.1f}')
              
    return

