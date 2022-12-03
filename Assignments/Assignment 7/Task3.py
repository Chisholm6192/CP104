"""
-------------------------------------------------------
Assignment 7 Task 3
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      *********
Email:   *********
__updated__ = "2022-11-16"
-------------------------------------------------------
"""

indexes = list_indexes([-2,5,7,2,9,0,2,4,6], 2)
print(indexes)



def list_indexes(values, target):
    """
    -------------------------------------------------------
    Finds the indexes of target in values.
    Use: indexes = list_indexes(values, target)
    -------------------------------------------------------
    Parameters:
        values - list of value (list of int)
        target - value to look for in num_list (int)
    Returns:
        locations - list of indexes of target (list of int)
    -------------------------------------------------------
    """
    indexes = []
    
    for i in range(0, len(values), 1):
        if values[i] == target:
            indexes.append(i)
            
    return indexes
