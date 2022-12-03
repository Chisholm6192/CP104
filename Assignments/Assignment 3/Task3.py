"""
-------------------------------------------------------
Assignment 3 Task 3
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      *********
Email:   *********
__updated__ = "2022-10-15"
-------------------------------------------------------
"""

date = int(input("Enter a date in the form MMDDYYYY: "))
year, month, day = date_extract(date)
print(f"\nThe reformatted date: {year:04d}/{month:02d}/{day:02d}")

def date_extract(date_number):
    """
    -------------------------------------------------------
    Extracts the year, month, and day from a date number in the format MMDDYYYY.
    Use: year, month, day = date_extract(date_number)
    -------------------------------------------------------
    Parameters:
        date_number - a date number in the format MMDDYYYY (int > 0)
    Returns:
        year - year portion of date_number (int)
        month - month portion of date_number (int)
        day - day portion of date_number (int)
    ------------------------------------------------------
    """
    month = date_number // 1000000 #separating the month number
    day = (date_number % 1000000) // 10000 #separating the day number from the month and year
    year = date_number % 10000 #separating the year number
    
    return (year, month, day)
