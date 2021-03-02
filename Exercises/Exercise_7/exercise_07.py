'''
Exercise 7: Sum of the First n Positive Integers

Stephenson, B., 2014. The Python workbook A Brief
Introduction with Exercises and Solutions. New York
Dordrecht London: Springer.
'''
def add_to( n ):
    sum=0
    for x in range (n+1):
        sum+=x

    return sum


n = int( input("input the upper limit  to sum:") )

print( f"The sum form zero to {n} is: {add_to(n)}" )
