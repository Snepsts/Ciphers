#!/usr/bin/python3

#Author: Jonathon Bryant

import re

#Function that takes user input and turns it into a list with only letters
def Clist(info):
    listLen = len(info)
    temp = ""

    for i in range(0,listLen):
        if bool(re.compile('[a-z]').match(info[i])) == True:
            temp += info[i]

    return temp

#Function for displaying the steps of each cipher
def DisplayList(ListInfo):
    listlen = len(ListInfo)
    for i in range(0,listlen):
        print(ListInfo[i], end=" ")
    print("")

#Function for converting letters into the coresponding numbers
def numbers(plaintext):
    temp = []
    listlen = len(plaintext)

    for i in range(0,listlen):
        num = ord(plaintext[i]) #change a-z to 97-122
        if num < 97 or num > 122:
            print("Something went wrong")
        else:
            num -= 97 #change 97-122 to 0-25
            temp.append(num)

    return temp

#Function for computing the numbers for the ciphertext
def eNumbers(nText, a, b):
    temp = []
    listlen = len(nText)

    for i in range(0,listlen):
        new = (int(a) * int(nText[i]) + int(b)) % 26
        temp.append(new)

    return temp

#Function for turning the converted numbers to the ciphertext
def cChar(eText):
    temp = []
    listlen = len(eText)

    for i in range(0,listlen):
        num = eText[i]
        if num < 0 or num > 25:
            print("Something went wrong")
        else:
            num += 65 #change 0-25 to A-Z
            temp.append(chr(num))

    return temp

#This is the function for all the ciphers
def Affine(a, b):
    print("Enter a sentence to encrypt")
    info = input()
    info = info.lower()
    sentence = Clist(info)
    print(sentence)
    plaintext = list(sentence)
    DisplayList(plaintext)
    nText = numbers(plaintext)
    DisplayList(nText)
    eText = eNumbers(nText, a, b)
    DisplayList(eText)
    ciphertext = cChar(eText)
    DisplayList(ciphertext)

#This is the main function for the program
def main():
    print("What cipher do you want to use?")
    print("1.Shift\n2.Multiplicative\n3.Affine")
    choice = input()
    if choice == '1':
        print("What is your b?")
        b = input()
        Affine(1,b)
    elif choice == '2':
        print("What is your a")
        a = input()
        Affine(a,0)
    elif choice == '3':
        print("What is your a?")
        a = input()
        print("What is your b?")
        b = input()
        Affine(a,b)

if __name__ == '__main__':
    main()
