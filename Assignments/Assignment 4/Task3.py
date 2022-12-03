"""
-------------------------------------------------------
Assignment 4 Task 3
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      *********
Email:   *********
__updated__ = "2022-10-26"
-------------------------------------------------------
"""

product = product_largest(2,3,0)
print(product)


def product_largest(v1, v2, v3):
    """
    -------------------------------------------------------
    Returns the product of the two largest values of
    v1, v2, and v3.
    Use: product = product_largest(v1, v2, v3)
    -------------------------------------------------------
    Parameters:
        v1 - a number (float)
        v2 - a number (float)
        v3 - a number (float)
    Returns:
        product - the product of the two largest values of
            v1, v2, and v3 (float)
    ------------------------------------------------------
    """    
    if v1 > v2:
        if v2 > v3:
            product = v1 * v2
        
        elif v3 > v2:
            product = v1 * v3
            
        elif v2 == v3:
            product = v1 * v3
            
    elif v2 > v1:
        if v1 > v3:
            product = v2 * v1
        
        elif v3 > v1:
            product = v2 * v3
            
        elif v3 == v1:
            product = v2 * v3
            
    elif v2 == v1:
        if v3 > v2:
            product = v1 * v3
            
        elif v3 < v2:
            product = v1 * v2
            
        elif v2 == v3:
            product = v1 * v2
            
            
    return product
