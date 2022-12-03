"""
-------------------------------------------------------
Assignment 5 Task 4
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      *********
Email:   *********
__updated__ = "2022-11-04"
-------------------------------------------------------
"""

multiplication_table(10, 15)



def multiplication_table(start, stop):
    """
    -------------------------------------------------------
    Prints a multiplication table for values from start to stop.
    Use: multiplication_table(start, stop)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        stop - the range stop value (int)
    Returns:
        None
    ------------------------------------------------------
    """
    space = "-----" 
    number = (stop - start) + 1
     
    for i in range(start, stop + 1): #for loop for printing first layer of numbers above the table
        
        if i == start:
            print(f"       {i:>5}", end = "")
            
        else:
            print(f"{i:>5}", end = "")
            
    print() #new line
    print(f"       {space * number}")
    
    for i in range(start, stop + 1):
        
        print(f"{i:>5} |", end="") #printing the row numbers with vertical line
        
        for j in range(start, stop+1):
            
            print(f"{i * j:>5}", end = "") #printing the products of the multiplication
            
        print() #new line
    
            
    return
