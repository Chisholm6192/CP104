"""
-------------------------------------------------------
Assignment 2 Task 1
-------------------------------------------------------
Author:  Ryan Chisholm
ID:      *********
Email:   *********
__updated__ = "2022-10-02"
-------------------------------------------------------
"""
# Imports

# Constants
TAX = 0.185 #constant for the rate of tax 

sales = float(input("Enter the total sales: $"))
tax = TAX * sales #total taxes is the tax rate multiplied by the total sales
taxes = TAX * 100 #taxes as a percent integer, needs to be multiplied by 100

print(f"\nProjected Tax Report")
print("--------------------------")
print(f"Total sales:   $ {sales:,.02f}")
print(f"Annual tax:    % {taxes:.02f}")
print("--------------------------")
print(f"Tax:           $  {tax:,.02f}")

