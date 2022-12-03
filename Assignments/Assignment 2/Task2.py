"""
-------------------------------------------------------
Assignment 2 Task 2
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      *********
Email:   *********
__updated__ = "2022-10-03"
-------------------------------------------------------
"""
# Imports

# Constants
    
num = int(input("Enter a positive digit number: "))
num1 = num // 10 #integer division to find the value of the tens column
num2 = num % 10 #remainder of integer division to find the value of the ones column
product = num1 * num2
print(f"\nThe product of the digits of {num} is {product}")



