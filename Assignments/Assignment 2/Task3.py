"""
-------------------------------------------------------
Assignment 2 Task 3
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      *********
Email:   *********
__updated__ = "2022-10-03"
-------------------------------------------------------
"""
# Imports

# Constants

date = int(input("Enter a date in the format DDMMYYYY: ")) #input of date in numeric form

year = date % 10000 #calculation of date from last 4 digits of input

month_and_year = date % 1000000 #calculating the remainders in the input

month = month_and_year // 10000 #taking the remainders and calculating months from it

day = date // 1000000 #calculation of days from input

print(f"\nThe reformatted date: {year:04d}/{month:02d}/{day:02d}")
