#!/usr/bin/env python3

if __name__ == '__main__':
    _ = int(input())
    arr = list(map(int, input().rstrip().split()))
    print(*list(reversed(arr)), sep=" ")
    # or print(*list(arr[::-1]))
