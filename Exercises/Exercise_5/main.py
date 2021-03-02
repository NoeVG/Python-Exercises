'''
Exercise 5: Bottle Deposits

Stephenson, B., 2014. The Python workbook A Brief
Introduction with Exercises and Solutions. New York
Dordrecht London: Springer.
'''

def main():
    deposit = 0.0             # total $ of the deposit
    botles = 0.0              # numbers of botles
    typeBottle = '1'          # option to type of the bottles

    # print message
    print("Bottle Deposits")
    # start the try catch to exit of the program with ctrl + c
    try:
        # loop to get the inputs
        while True:
            # reset the numbers of botles
            botles = 0
            # print message instructions
            print("Finish deposit with ctrl + c")
            print("Select the input the type: ")
            print(" 1 = one liter or less")
            print(" 2 = more than one liter")
            # Get data from user to type bottle
            typeBottle = input()
            # print message instructions
            print("Input the number of bottles: ")
            # Get data from user to number of bottles
            botles = int(input())
            # if-elseif-else to select deposit
            if typeBottle == '1':
                # multiply
                deposit += (0.10 * botles)
            elif typeBottle == '2':
                # multiply
                deposit += (0.25 * botles)
            else:
                # message of select not recognized in the type bottle
                print("Bottle type not recognized")
            # print message total deposit only two decimals
            print("Total deposit: $ %0.2f"%deposit)
    # when the user press ctrl + c the program exit
    except KeyboardInterrupt:
        print("Bye... !")

# main function
if __name__ == "__main__":
    main()
