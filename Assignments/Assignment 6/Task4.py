"""
-------------------------------------------------------
Assignment 6 Task 4
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      *********
Email:   *********
__updated__ = "2022-11-11"
-------------------------------------------------------
"""

count = digit_count(120)
print(count)


def digit_count(num):
    """
    -------------------------------------------------------
    Counts the number of digits in an integer.
    Use: count = digit_count(num)
    -------------------------------------------------------
    Parameters:
        num - an integer (int)
    Returns:
        count - the number of digits in num (int)
    ------------------------------------------------------
    """
    n = 1
    digits = 0
    
    while num / n >= 1 or num / n <= -1:
        digits += 1
        n *= 10 
        
    if num == 0:
        digits = 1
        
    return digits
