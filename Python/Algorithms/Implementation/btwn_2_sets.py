#!/usr/bin/env python3


def gcd(a, b):
    a_int = isinstance(a, int)
    b_int = isinstance(b, int)
    a = abs(a)
    b = abs(b)
    if not(a_int or b_int):
        raise ValueError("Input arguments are not integers")
    if (a == 0) or (b == 0):
        raise ValueError("One or more input arguments equals zero")
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Computes the lowest common multiple of integers a and b."""
    return abs(a) * abs(b) // gcd(a, b)


def getTotalX(a, b):
    lcm_a = a[0]
    for i in a:
        lcm_a = lcm(lcm_a, i)

    hcf_b = b[0]
    for i in b:
        hcf = gcd(hcf_b, i)

    sum_num_exist = 0
    for i in range(lcm_a, hcf_b+1, lcm_a):
        remainder = (hcf_b % i) + (i % lcm_a)
        if not remainder:
            sum_num_exist += 1
    return sum_num_exist


if __name__ == '__main__':
    _, _ = input().rstrip().split()
    arr = list(map(int, input().rstrip().split()))
    brr = list(map(int, input().rstrip().split()))
    total = getTotalX(arr, brr)
    print(total)