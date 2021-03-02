'''
Exercise 80: Coin Flip Simulation

Stephenson, B., 2014. The Python workbook A Brief
Introduction with Exercises and Solutions. New York
Dordrecht London: Springer.
'''
import random as rnd


def flip_coin():
    return rnd.choice( ['H','T'] )


print("\n")
print("-"*40)
print("--- FLIP COINS ---".center(40))
print("-"*40)

mean = 0
for _ in range(10):
    sequence = flip_coin()
    count = 1
    while count != 3:
        coin = flip_coin()
        if coin == sequence[-1]:
            count += 1
        else:
            count = 1
        sequence += coin
    print( sequence, f" ({len(sequence)} flips)")
    mean +=  len(sequence)

mean /= 10

print("-"*10)
print(f"on average, {mean} flips were needed." )

print("\n")
