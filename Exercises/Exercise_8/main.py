'''
Exercise 8: Widgets and Gizmos

Stephenson, B., 2014. The Python workbook A Brief
Introduction with Exercises and Solutions. New York
Dordrecht London: Springer.
'''

def main():
    typeItem = ''       # Type Item (Widgets / Gizmos)
    weightItem = 0.0    # Weight Item (75 or 112 grams)
    items = 0           # Numbes of items
    weightTotal = 0.0   # Weight total grams

    # print message
    print("Widgets and Gizmos")
    print("Select the item type: ")
    print(" 1 = Widgets")
    print(" 2 = Gizmos")
    # input the type item
    typeItem = input()
    # if-else about type item
    if(typeItem == '1'):
        # set the Weight to Widgets
        weightItem = 75
    else:
        # set the Weight to Gizmos
        weightItem = 112
    # print the get numbers items message
    print("Input the number of items: ")
    # input the numbers of items
    items = int(input())
    # compute the Weight total
    weightTotal = items * weightItem
    # print message result
    print("Weight total: %0.2f grams"%weightTotal)

# main function
if __name__ == "__main__":
    main()
