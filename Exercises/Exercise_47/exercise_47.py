'''
Exercise 47: Birth Date to Astrological Sign

Stephenson, B., 2014. The Python workbook A Brief
Introduction with Exercises and Solutions. New York
Dordrecht London: Springer.
'''

birth_month = input( "Input your birth month: " ).lower()
birth_day = int( input( "Input your birth day: ") )

month = ["january", "february", "march", "april",  "may",
  "june", "july", "august", "september", "october",
  "november", "december" ]

cut_day = [19, 18, 20, 19, 20,
         20, 22, 22, 22, 22,
         21, 21 ]

astrological_sign = ["Capricorn", "Aquarius", "Pisces", "Aries", "Taurus",
          "Gemini",  "Cancer",  "Leo", "Virgo", "Libra",
          "Scorpio", "Sagittarius" ]

idx = month.index( birth_month )

if birth_day <= cut_day[ idx ]:
    sign = astrological_sign[idx]
else:
    sign = astrological_sign[ (idx+1)%12 ]

print("Your Zodiacal sign is: ", sign )
