'''
Exercise 3: Area of a Room

Stephenson, B., 2014. The Python workbook A Brief
Introduction with Exercises and Solutions. New York
Dordrecht London: Springer.
'''

def main():
    width = 0.0
    length = 0.0
    area = 0.0
    print("Area Room")
    print("Please input values of width (meters)")
    width = float ( input() )
    print("Please input values of length (meters)")
    length = float ( input() )
    area = width * length
    print("Area (meters) :",area)


if __name__ == "__main__":
    main()
