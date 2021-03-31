#!/usr/bin/env python3

IRET = 0
IDUE = 1
IDATE = 0
IMONTH = 1
IYEAR = 2


if __name__ == '__main__':
    """ NESTED LIST LOGIC
    @param  `date` nested list type. In this list we have date when
            returned book `IRET` and due date `IDUE`.
            Both this data in format `[IDATE, IMONTH, IYEAR]`.
    @returns integer denoting the library fine for the book received as input.
    """
    date = [list(map(int, input().strip().split(' '))) for _ in range(2)]
    if date[IDUE][::-1] >= date[IRET][::-1]:
        print(0)
    elif date[IDUE][IMONTH:] == date[IRET][IMONTH:]:
        print(15 * abs(date[IRET][IDATE] - date[IDUE][IDATE]))
    elif date[IDUE][IYEAR] == date[IRET][IYEAR]:
        print(500 * abs(date[IRET][IMONTH] - date[IDUE][IMONTH]))
    else:
        print(10_000)
