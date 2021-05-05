#!/usr/bin/env python3


def countApplesAndOranges(s, t, a, b, apples, oranges):
    sum_apple = sum([1 for x in apples if (s <= (x + a) <= t)])
    sum_orange = sum([1 for y in oranges if (s <= (y + b) <= t)])
    print(sum_apple, sum_orange, sep='\n')

if __name__ == '__main__':
    st_input = input().rstrip().split()
    s = int(st_input[0])
    t = int(st_input[1])
    ab_input = input().rstrip().split()
    a = int(ab_input[0])
    b = int(ab_input[1])
    _ = input().rstrip().split()
    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))
    countApplesAndOranges(s, t, a, b, apples, oranges)