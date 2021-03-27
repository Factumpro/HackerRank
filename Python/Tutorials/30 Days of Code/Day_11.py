#!/usr/bin/env python3

"""
    >>>
        1 1 1 0 0 0
        0 1 0 0 0 0
        1 1 1 0 0 0
        0 0 2 4 4 0
        0 0 0 2 0 0
        0 0 1 2 4 0
    '19'
"""

if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    hourglass_max = []
    for x in range(0, 4):
        for y in range(0, 4):
            abc = sum(arr[x][y:y+3])
            d = arr[x+1][y+1]
            efg = sum(arr[x+2][y:y+3])

            hourglass_sum = abc + d + efg
            hourglass_max.append(hourglass_sum)

    print(max(hourglass_max))
