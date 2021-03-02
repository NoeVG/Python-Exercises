'''
Exercise 6: Tax and Tip

Stephenson, B., 2014. The Python workbook A Brief
Introduction with Exercises and Solutions. New York
Dordrecht London: Springer.
'''
"""
> What is the price of the meal?
100
> Bill detail
---------------------
    order:  100.00
tax (16%):   16.00
tip (18%):   18.00
---------------------
    TOTAL:  134.00
"""
print("What is the price of the meal?" )
costo= float( input() )

tax=costo*0.16
tip=costo*0.18
total=costo+tax+tip

print("\nBill detail:")
print("-"*25)
print( f"{'cost':>12} : {costo:>8}",  )
print( f"{'Tax':>12} : {tax:>8}",  )
print( f"{'Tip':>12} : {tip:>8}",  )
print("-"*25)
print( f"{'TOTAL':>12} : {total:>8}",  )
