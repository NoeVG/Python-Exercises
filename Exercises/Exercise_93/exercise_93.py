'''
Exercise 93: Next Prime

Stephenson, B., 2014. The Python workbook A Brief
Introduction with Exercises and Solutions. New York
Dordrecht London: Springer.
'''
def is_prime( k ):
    for d in range(2,k):
        if k%d == 0:
            return False
    return True

def next_prime( n ):
    m = n+1
    while is_prime(m) == False:
        m += 1

    return m


n = int(input("Input a integer number: "))
print(f"The next prime to  {n} is: ", next_prime(n)  )
