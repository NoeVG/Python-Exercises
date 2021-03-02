'''
Exercise 70: Caesar Cipher

Stephenson, B., 2014. The Python workbook A Brief
Introduction with Exercises and Solutions. New York
Dordrecht London: Springer.
'''

def encrypt( message, key ):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz"

    message_encrypted = ""
    for letter in message:
        idx = alphabet.index( letter )
        message_encrypted += alphabet[ (idx+key)%len(alphabet) ]

    return message_encrypted

message = input("Input a message to encrypt: ")
key = int(input("Input a key to encrypt: "))

print("encrypted message: ",encrypt(message,key))
