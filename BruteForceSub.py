#!/usr/bin/python3

LtN = {'A':0,
       'B':1,
       'C':2,
       'D':3,
       'E':4,
       'F':5,
       'G':6,
       'H':7,
       'I':8,
       'J':9,
       'K':10,
       'L':11,
       'M':12,
       'N':13,
       'O':14,
       'P':15,
       'Q':16,
       'R':17,
       'S':18,
       'T':19,
       'U':20,
       'V':21,
       'W':22,
       'X':23,
       'Y':24,
       'Z':25}

def ConvertLtN(Lct):
    for x in range(0,len(Lct)):
        for key, value in LtN.items():
            if Lct[x] == key:
                Lct[x] = value

    return Lct

def ConvertNtL(Lct):
    for x in range(0,len(Lct)):
        for key, value in LtN.items():
            if Lct[x] == value:
                Lct[x] = key

    return Lct

def main():
    print("What is the ciphertext?")
    ct = input()
    ct = ct.upper()

    for x in range(0,26):
        Lct = list(ct)
        Lct = ConvertLtN(Lct)
        for y in range(0,len(Lct)):
            Lct[y] = (Lct[y] + x) % 26
        Lct = ConvertNtL(Lct)
        print("".join(Lct))

if __name__ == '__main__':
    main()
