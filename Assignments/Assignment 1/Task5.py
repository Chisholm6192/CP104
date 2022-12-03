"""
-------------------------------------------------------
Assignment 1 Task 5
Program takes mortgage amount, interest, length of mortgage(in years), and number of times the
interest is compounded per year, and outputs the total amount owing for the mortgage, with interest included
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      *********
Email:   *********
__updated__ = "2022-09-26"
-------------------------------------------------------
"""
# Imports

# Constants

P = float(input("Principal: $")) #principal mortgage amount
r = float(input("Interest (decimal): ")) #annual interest rate
t = int(input("Number of years: ")) #number of years that the mortgage is for
n = int(input("Number of times interest compounded per year: ")) #how many times the interest is compounded per year
    
A = P*((1 + (r/n))**(n*t)) #calculation to find the balance owing, after interest is added in
print(f"Balance: $ {A}")
