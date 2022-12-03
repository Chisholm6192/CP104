"""
-------------------------------------------------------
Assignment 6 Task 3
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      *********
Email:   *********
__updated__ = "2022-11-11"
-------------------------------------------------------
"""


interest_table(1000, 10, 100)




def interest_table(principal, rate, payment):
    """
    -------------------------------------------------------
    Prints a table of monthly interest and payments on a loan.
    Use: interest_table(principal, rate, payment)
    -------------------------------------------------------
    Parameters:
        principal - original value of a loan (float > 0)
        rate - yearly interest rate as a % (float >= 0)
        payment - the monthly payment (float > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    month = 1
    print(f'Principal:   ${principal:.2f}')
    print(f'Interest rate : {rate:.1f}%')
    print(f'Monthly payment: ${payment:.2f}')
    print('----------------------------------')
    print(f'Month Interest   Payment   Balance')
    print('----------------------------------')
    
    while principal > 0: #runs until the debt is paid off
        interest = (principal * (rate / 100)) / 12
        
        if principal < payment: #if on the final payment
            payment = principal + interest
        
        principal = (principal + interest) - payment #updated balance
        
        print(f'{month:5d}{interest:9.2f}{payment:10.2f}{principal:10.2f}')
        
        month += 1
        
    return
