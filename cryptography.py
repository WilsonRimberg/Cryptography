"""
cryptography.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
associations1="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
command=str(input("Enter e to encrypt, d to decrypt, or q to quit: "))
while command not in ["e","d","q"]:
    print("Did not understand command, try again.")
    command=input("Enter e to encrypt, d to decrypt, or q to quit: ")
if command== "q":
    print("Goodbye!")
while command =="e":
    message1=input("Message: ")
    message=list(message1)
    key1=input("Key: ")
    key= list(key1)
    for x in range(0, len(message)):
        message[x]=associations.find(message[x])
    for x in range(0, len(key)):
        key[x]=associations.find(key[x])
    while len(key)<len(message):
        key.extend(key)
    added=[x+y for x,y in zip(message, key)]
    for x in range(0, len(message)):
        bob=associations1[added[x]]
        print(bob,end="")
    print( )
    command=input("Enter e to encrypt, d to decrypt, or q to quit: ")
while command=="d":
    message1=input("Message: ")
    message=list(message1)
    key1=input("Key: ")
    key= list(key1)
    for x in range(0, len(message)):
        message[x]=associations.find(message[x])
    for x in range(0, len(key)):
        key[x]=associations.find(key[x])
    while len(key)<len(message):
        key.extend(key)
    added=[x-y for x,y in zip(message, key)]
    for x in range(0, len(message)):
        bob=associations1[added[x]]
        print(bob,end="")
    print( )
    command=input("Enter e to encrypt, d to decrypt, or q to quit: ")
    
    