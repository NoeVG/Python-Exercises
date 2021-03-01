'''
Exercise 4: Area of a Field

Stephenson, B., 2014. The Python workbook A Brief
Introduction with Exercises and Solutions. New York
Dordrecht London: Springer.
'''

def main():
    width = 0.0
    length = 0.0
    area = 0.0
    print("Area of a Field")
    print("Please input values of width (feet)")
    width = float ( input() )
    print("Please input values of length (feet)")
    length = float ( input() )
    area = width * length
    area = area / 43560
    print("Area (acre) : %.4f" % area)


if __name__ == "__main__":
    main()
