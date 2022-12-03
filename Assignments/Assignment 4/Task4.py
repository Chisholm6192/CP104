"""
-------------------------------------------------------
Assignment 4 Task 4
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      *********
Email:   *********
__updated__ = "2022-10-26"
-------------------------------------------------------
"""

colour = rgb_mix("green", "fuchsia")
print(colour)


def rgb_mix(rgb1, rgb2):
    """
    -------------------------------------------------------
    Determines the secondary colour from mixing two primary
    RGB (Red, Green, Blue) colours. The order of the colours
    is *not* significant.
    Returns "Error" if any of the colour parameter(s) are invalid.
        "red" + "blue": "fuchsia"
        "red" + "green": "yellow"
        "green" + "blue": "aqua"
        "red" + "red": "red"
        "blue" + "blue": "blue"
        "green" + "green": "green"
    Use: colour = rgb_mix(rgb1, rgb2)
    -------------------------------------------------------
    Parameters:
        rgb1 - a primary RGB colour (str)
        rgb2 - a primary RGB colour (str)
    Returns:
        colour - a secondary RGB colour (str)
    -------------------------------------------------------
    """
    colour = ""
        
    if rgb1 == "red":
        if rgb2 == "blue":
            colour = "fuchsia"
        
        elif rgb2 == "green":
            colour = "yellow"
            
        elif rgb1 == rgb2:
            colour = rgb1
            
        else:
            colour = "Error"
            
    elif rgb1 == "blue":
        if rgb2 == "red":
            colour = "fuchsia"
            
        elif rgb2 == "green":
            colour = "aqua"
            
        elif rgb1 == rgb2:
            colour = rgb1
        
        else:
            colour = "Error"
        
    elif rgb1 == "green":
        if rgb2 == "red":
            colour = "yellow"
            
        elif rgb2 == "blue":
            colour = "aqua"
            
        elif rgb1 == rgb2:
            colour = rgb1
            
        else:
            colour = "Error"
        
    else:
        colour = "Error"
            
    return colour
