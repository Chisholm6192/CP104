"""
-------------------------------------------------------
Assignment 6 Task 2
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      *********
Email:   *********
__updated__ = "2022-11-11"
-------------------------------------------------------
"""

prime = is_prime(4)
print(prime)



def is_prime(num):
    """
    -------------------------------------------------------
    Determines if num is a prime number.
    Use: prime = is_prime(num)
    -------------------------------------------------------
    Parameters:
        num - a positive integer (int > 1)
    Returns:
        prime - True if num is prime, False otherwise (bool)
    ------------------------------------------------------
    """
    n = 1
    prime = True
    
    while n < num: #run until all values from 1 to 'num' have been checked
        if(num % n == 0) and num != n and n != 1:    
            prime = False 
            
        n += 1
            
    if num <= 1:
        prime = False
        
    return prime
