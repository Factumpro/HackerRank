#!/usr/bin/env python3


def kangaroo(x1, v1, x2, v2):
    # x1-x2 = y*(v2-v1)
    # x1 + v1*y = x2 + v2*y
    first_point = abs((x1+v1)-(x2+v2))
    second_point = abs((x1+v1+v1)-(x2+v2+v2))
    first_point_isNull = not first_point
    will_intersect = not ((x1-x2) % (v2-v1))
    if first_point > second_point or first_point_isNull and will_intersect:
        return "YES"
    return "NO"

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    x1 = int(first_multiple_input[0])
    v1 = int(first_multiple_input[1])
    x2 = int(first_multiple_input[2])
    v2 = int(first_multiple_input[3])
    result = kangaroo(x1, v1, x2, v2)
    print(result)