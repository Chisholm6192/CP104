"""
-------------------------------------------------------
Assignment 7 Task 2
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      *********
Email:   *********
__updated__ = "2022-11-16"
-------------------------------------------------------
"""

numbers = list_positives()
print(numbers)


def list_positives():
    """
    -------------------------------------------------------
    Gets a list of positive numbers from a user.
    Negative numbers are ignored. Enter 0 to stop entries.
    Use: numbers = list_positives()
    -------------------------------------------------------
    Returns:
        numbers - A list of positive integers (list of int)
    ------------------------------------------------------
    """
    numbers = []
    positive = int(input("Enter a positive number: "))
    
    while positive != 0:
        if positive >= 1:
            numbers.append(positive)
            
        positive = int(input("Enter a positive number: "))
        
    return numbers
