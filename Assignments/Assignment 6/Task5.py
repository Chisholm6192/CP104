"""
-------------------------------------------------------
Assignment 6 Task 5
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      *********
Email:   *********
__updated__ = "2022-11-11"
-------------------------------------------------------
"""

total = sum_factors(120)
print(total)


def sum_factors(num):
    """
    -------------------------------------------------------
    Determines the sum of factors of an integer not including
    the integer itself. An integer's factors are the whole numbers
    that the integer can be evenly divided by.
    Use: total = sum_factors(num)
    -------------------------------------------------------
    Parameters:
        num - a positive integer (int >= 1)
    Returns:
        total - the total of num's factors (int)
    ------------------------------------------------------
    """
    n = 1
    total = 0
    
    while n < num: #check all values up to 'num'
        if num % n == 0:
            total += n #each value that is a factor of n gets added to the total
            
        n += 1
        
    return total
