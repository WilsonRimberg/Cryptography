"""
cryptography.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
command=str(input("Enter e to encrypt, d to decrypt, or q to quit: "))
while command not in ["e","d","q"]:
    print("Did not understand command, try again.")
    command=input("Enter e to encrypt, d to decrypt, or q to quit: ")
if command== "q":
    print("Goodbye!")
if command =="e":
    message=list(input("Message: "))
    key= list(input("Key: "))
    for x in range(0, len(message)):
        message[x]=associations.find(message[x])
    for x in range(0, len(key)):
        key[x]=associations.find(key[x])
    if len(key)<len(message)
    