#!/usr/bin/env python3

if __name__ == '__main__':
    _ = int(input())
    integer_list = map(int, input().split())
    tulp = tuple(integer_list)
    print(hash(tulp))
