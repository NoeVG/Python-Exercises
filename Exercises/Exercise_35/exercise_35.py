'''
Exercise 35: Dog Years

Stephenson, B., 2014. The Python workbook A Brief
Introduction with Exercises and Solutions. New York
Dordrecht London: Springer.
'''
def human_to_dog_age( human_years ):
    dog_years = 0

    if human_years < 3:
        dog_years =  human_years*10.5
    else:
        # first two human years are 21 dog years
        dog_years = 21
        # remain years are 4 years for 1 human year
        dog_years =  dog_years +  (human_years-2)*4

    return dog_years

human_years = int( input("Input human years: ") )
print(f"{human_years} human years are {human_to_dog_age(human_years)} dog years")
