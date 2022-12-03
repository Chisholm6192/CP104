"""
-------------------------------------------------------
Assignment 7 Task 4
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      *********
Email:   *********
__updated__ = "2022-11-16"
-------------------------------------------------------
"""

minuend = [1,2,3,4,5,6,1]
subtract_lists(minuend, [1, 4, 6])
print(minuend)



def subtract_lists(minuend, subtrahend):
    """
    -------------------------------------------------------
    Updates the list minuend removing from it the values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are not included in the updated list.
    subtrahend is unchanged
    Use: subtract_lists(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to remove from minuend (list)
    Returns:
        None
    ------------------------------------------------------
    """
    removal = []
    
    for i in subtrahend:
        for j in minuend:
            if j == i:
                removal.append(j)
                
        
    for i in removal:
        minuend.remove(i)
                                               
    return
