#!/usr/bin/env python3

if __name__ == '__main__':
    Num = int(input())
    if (Num % 2 == 0 and
            Num not in range(6, 21)):
        print ("Not", end=" "),
    print("Weird")
