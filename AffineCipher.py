#!/usr/bin/python3

import re

def Clist(info):
    listLen = len(info)
    temp = ""

    for i in range(0,listLen):
        if bool(re.compile('[a-z]').match(info[i])) == True:
            temp += info[i]

    return temp

def DisplayList(ListInfo):
    listlen = len(ListInfo)
    for i in range(0,listlen):
        print(ListInfo[i], end=" ")
    print("")

def numbers(plaintext):
    temp = []
    listlen = len(plaintext)

    for i in range(0,listlen):
        if plaintext[i] == 'a':
            temp.append(0)
        elif plaintext[i] == 'b':
            temp.append(1)
        elif plaintext[i] == 'c':
            temp.append(2)
        elif plaintext[i] == 'd':
            temp.append(3)
        elif plaintext[i] == 'e':
            temp.append(4)
        elif plaintext[i] == 'f':
            temp.append(5)
        elif plaintext[i] == 'g':
            temp.append(6)
        elif plaintext[i] == 'h':
            temp.append(7)
        elif plaintext[i] == 'i':
            temp.append(8)
        elif plaintext[i] == 'j':
            temp.append(9)
        elif plaintext[i] == 'k':
            temp.append(10)
        elif plaintext[i] == 'l':
            temp.append(11)
        elif plaintext[i] == 'm':
            temp.append(12)
        elif plaintext[i] == 'n':
            temp.append(13)
        elif plaintext[i] == 'o':
            temp.append(14)
        elif plaintext[i] == 'p':
            temp.append(15)
        elif plaintext[i] == 'q':
            temp.append(16)
        elif plaintext[i] == 'r':
            temp.append(17)
        elif plaintext[i] == 's':
            temp.append(18)
        elif plaintext[i] == 't':
            temp.append(19)
        elif plaintext[i] == 'u':
            temp.append(20)
        elif plaintext[i] == 'v':
            temp.append(21)
        elif plaintext[i] == 'w':
            temp.append(22)
        elif plaintext[i] == 'x':
            temp.append(23)
        elif plaintext[i] == 'y':
            temp.append(24)
        elif plaintext[i] == 'z':
            temp.append(25)
        else:
            print("Something went wrong")

    return temp

def eNumbers(nText, a, b):
    temp = []
    listlen = len(nText)

    for i in range(0,listlen):
        new = (int(a) * int(nText[i]) + int(b)) % 26
        temp.append(new)

    return temp

def cChar(eText):
    temp = []
    listlen = len(eText)

    for i in range(0,listlen):
        if eText[i] == 0:
            temp.append('A')
        elif eText[i] == 1:
            temp.append('B')
        elif eText[i] == 2:
            temp.append('C')
        elif eText[i] == 3:
            temp.append('D')
        elif eText[i] == 4:
            temp.append('E')
        elif eText[i] == 5:
            temp.append('F')
        elif eText[i] == 6:
            temp.append('G')
        elif eText[i] == 7:
            temp.append('H')
        elif eText[i] == 8:
            temp.append('I')
        elif eText[i] == 9:
            temp.append('J')
        elif eText[i] == 10:
            temp.append('K')
        elif eText[i] == 11:
            temp.append('L')
        elif eText[i] == 12:
            temp.append('M')
        elif eText[i] == 13:
            temp.append('N')
        elif eText[i] == 14:
            temp.append('O')
        elif eText[i] == 15:
            temp.append('P')
        elif eText[i] == 16:
            temp.append('Q')
        elif eText[i] == 17:
            temp.append('R')
        elif eText[i] == 18:
            temp.append('S')
        elif eText[i] == 19:
            temp.append('T')
        elif eText[i] == 20:
            temp.append('U')
        elif eText[i] == 21:
            temp.append('V')
        elif eText[i] == 22:
            temp.append('W')
        elif eText[i] == 23:
            temp.append('X')
        elif eText[i] == 24:
            temp.append('Y')
        elif eText[i] == 25:
            temp.append('Z')
        else:
            print("Someting went wrong")

    return temp

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
