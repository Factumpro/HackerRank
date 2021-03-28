#!/usr/bin/env python3

"""
    Bubble Sort
    -----------
    Time Complexity: O(n**2)

    Pseudo code:
    https://en.wikipedia.org/wiki/Bubble_sort#Pseudocode_implementation
"""

import sys


def bubbleSort(array_list):
    """
    Simple sorting algorithm that repeatedly steps through the list,
    compares adjacent elements and swaps them if they are in the wrong order.

    :input array_list: unsorted list of integers
    :output array_list: list of sorted integers
    :output swap_count: integer value of count swap iteration (need for task)
    """
    a_len = len(array_list)
    swap_count = 0
    for i in range(a_len):
        for n in range(1, a_len - i):
            if array_list[n-1] > array_list[n]:
                swap_count += 1
                array_list[n-1], array_list[n] = array_list[n], array_list[n-1]

    return array_list, swap_count

if __name__ == '__main__':
    _ = int(input().strip())
    unsorted_array = list(map(int, input().strip().split(" ")))
    sorted_array, swap_count = bubbleSort(unsorted_array)
    print(f'Array is sorted in {swap_count} swaps.')
    print(f'First Element: {sorted_array[0]}')
    print(f'Last Element: {sorted_array[-1]}')
