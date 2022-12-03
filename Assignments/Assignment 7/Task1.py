"""
-------------------------------------------------------
Assignment 7 Task 1
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      *********
Email:   *********
__updated__ = "2022-11-16"
-------------------------------------------------------
"""

factors = list_factors(9)
print(factors)

def list_factors(num):
    """
    -------------------------------------------------------
    Gets a list of all the factors of the given number, excluding the number itself
    Use: factors = list_factors(num)
    -------------------------------------------------------
    Parameters:
        num - the number that needs to be factorized (int > 0)
    Returns:
        factors - a list that contains all the factors of num (list of int)
    ------------------------------------------------------
    """
    factors = []
    
    for i in range(1, num, 1):
        if num % i == 0: #adds all evenly divisible numbers to list
            factors.append(i)
            
    return factors
