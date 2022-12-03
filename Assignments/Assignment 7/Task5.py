"""
-------------------------------------------------------
Assignment 7 Task 5
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      *********
Email:   *********
__updated__ = "2022-11-16"
-------------------------------------------------------
"""

in_order, index = is_sorted([1,2,3,4,5,4,6])
print(f'{in_order}, {index}')



def is_sorted(values):
    """
    -------------------------------------------------------
    Determines whether a list is sorted.
    Use: in_order, index = is_sorted(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list)
    Returns:
        in_order - True if values is sorted, False otherwise (bool)
        index - index of first value not in order,
            -1 if in_order is True (int)
    ------------------------------------------------------
    """
    in_order = True
    index = -1
                    
    for i in range(len(values) - 1):
        if values[i] > values[i + 1]:
            in_order = False
            index = i + 1
            break
                                 
    return (in_order, index)
