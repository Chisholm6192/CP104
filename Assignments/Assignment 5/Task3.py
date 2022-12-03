"""
-------------------------------------------------------
Assignment 5 Task 3
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      *********
Email:   *********
__updated__ = "2022-11-03"
-------------------------------------------------------
"""

open_triangle(4)


def open_triangle(num_rows):
    """
    -------------------------------------------------------
    Prints a triangle with the specified number of rows using the # symbol
    Use: open_triangle(num_rows)
    -------------------------------------------------------
    Parameters:
        num_rows - the number of rows to be printed (int > 0)
    Returns: None
    ------------------------------------------------------
    """
    space = " "
    
    for i in range(0, num_rows, 1):
        print(f'#{space * i}#')
        
    return
