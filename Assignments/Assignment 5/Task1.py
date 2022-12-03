"""
-------------------------------------------------------
Assignment 5 Task 1
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      *********
Email:   *********
__updated__ = "2022-11-03"
-------------------------------------------------------
"""

product = factorial(1)
print(product)


def factorial(num):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of num.
    Use: product = factorial(num)
    -------------------------------------------------------
    Parameters:
        num - number to factorial (int > 0)
    Returns:
        product - num! (int)
    ------------------------------------------------------
    """
    product = 1
    
    for i in range(1, num + 1, 1):
        product *= i
    
    return product
