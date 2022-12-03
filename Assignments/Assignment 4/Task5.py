"""
-------------------------------------------------------
Assignment 4 Task 5
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      *********
Email:   *********
__updated__ = "2022-10-26"
-------------------------------------------------------
"""

phrase = yee_ha(5)
print(phrase)


def yee_ha(number):
    """
    -------------------------------------------------------
    Prints different string output based on given integer input
    "Yee" : if number is evenly divisible by 3
    "Ha" : if number is evenly divisible by 7
    "Yee Ha" : if number is evenly divisible by both 3 and 7 
    "Nada" : if number is none of the above
    Use: phrase = yee_ha(number)
    -------------------------------------------------------
    Parameters:
    number - numeric input (int)
    Returns:
        phrase - the string output dependant upon the numeric input (str)
    -------------------------------------------------------
    """
    if number % 3 == 0 and number % 7 != 0:
        phrase = "Yee"
        
    elif number % 7 == 0 and number % 3 != 0:
        phrase = "Ha"
        
        
    elif number % 3 == 0 and number % 7 == 0:
        phrase = "Yee Ha"
        
    else:
        phrase = "Nada"
        
    return phrase
