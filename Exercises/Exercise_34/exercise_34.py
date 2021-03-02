'''
Exercise 34: Even or Odd?

Stephenson, B., 2014. The Python workbook A Brief
Introduction with Exercises and Solutions. New York
Dordrecht London: Springer.
'''
"""
Write a program that reads an integer from the user.
Then your program should display a message indicating
whether the integer is even or odd.
"""

n = int( input("input a integer number: ") )

if n % 2 == 0:  # is even?
    print("the number is even")
else:
    print("the number is odd")
