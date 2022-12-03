"""
-------------------------------------------------------
Assignment 6 Task 1
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      *********
Email:   *********
__updated__ = "2022-11-09"
-------------------------------------------------------
"""

count = winner()
print(count)


def winner():
    """
    -------------------------------------------------------
    Returns the number of times each input appears
    Use: count = winner()
    -------------------------------------------------------
    Parameters: None
    Returns: 
        blue - number of occurrences of 'blue' in list (int)
        grey - number of occurrences of 'grey' in list (int)
    -------------------------------------------------------
    """
    teams = []
    team = str(input("Enter the winning team: "))
        
    while team != "":
        teams.append(team) #add previous input to list
        team = str(input("Enter the winning team: "))  
        
    #count entries of 'blue' and 'grey'   
    blue = teams.count('blue')
    grey = teams.count('grey')
    
    return (blue, grey)
