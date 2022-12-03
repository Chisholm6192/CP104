"""
-------------------------------------------------------
Assignment 4 Task 2
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      *********  
Email:   *********
__updated__ = "2022-10-26"
-------------------------------------------------------
"""

level = pollution_level(-1)
print(level)

def pollution_level(aqi):
    """
    -------------------------------------------------------
    Returns the pollution level given an AQI (Air Quality Index):
        "Good" - 0 to 50 AQI
        "Moderate" - 51 - 100 AQI
        "Unhealthy for Sensitive Groups" - 101 - 150 AQI
        "Unhealthy" - 151 - 200 AQI
        "Very Unhealthy" - 201 - 300 AQI
        "Hazardous" - 300+ AQI
    Returns "Error" if aqi is negative.
    Use: level = pollution_level(aqi)
    -------------------------------------------------------
    Parameters:
        aqi - Air Quality Index (int)
    Returns:
        level - name of pollution level (str)
    ------------------------------------------------------
    """
    if aqi >= 0:
        if aqi <= 50:
            level = "Good"
        
        elif aqi >= 51 and aqi <= 100:
            level = "Moderate"
            
        elif aqi >= 101 and aqi <= 150:
            level = "Unhealthy for Sensitive Groups"
            
        elif aqi >= 151 and aqi <= 200:
            level = "Unhealthy"
            
        elif aqi >= 201 and aqi <= 300:
            level = "Very Unhealthy"
            
        else:
            level = "Hazardous"
          
    else: 
        level = "Error"
        
    return level
