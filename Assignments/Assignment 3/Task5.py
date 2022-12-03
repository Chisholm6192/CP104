"""
-------------------------------------------------------
Assignment 3 Task 5
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      *********
Email:   *********
__updated__ = "2022-10-15"
-------------------------------------------------------
"""
# Imports
from random import randint

math_quiz()

def math_quiz():
    """
    -------------------------------------------------------
    Gives user a sample math question to solve
    Use: math_quiz()
    -------------------------------------------------------
    Parameters: None
    Returns: None
    ------------------------------------------------------
    """
    num1 = randint(0,999)
    num2 = randint(0,999)
    answer = num1 + num2
    
    print(f"  {num1}\n+ {num2}\n")
    user_answer = int(input("Your answer: "))
    print(f"\nYour answer:    {user_answer}")
    print(f"Expected:    {answer}")
    
    return
