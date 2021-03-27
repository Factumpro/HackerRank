#!/usr/bin/env python3

for i in range(int(input())):
    s = input()
    step = 2
    print(*[''.join(s[:: step]), ''.join((s[1:: step]))])
