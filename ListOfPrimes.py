#!/usr/bin/python3

from fractions import gcd

def main():
    print("Enter number")
    num = input()
    num = int(num)

    count = 0

    for x in range(0,num):
        temp = gcd(x,num)
        if temp == 1:
            count = count + 1
            print(x)

    print(str(count))

if __name__ == '__main__':
    main()
