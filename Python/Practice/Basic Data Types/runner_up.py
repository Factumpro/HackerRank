#!/usr/bin/env python3

SECOND_PLACE = 1

if __name__ == '__main__':
    _ = int(input())
    runner_scores = list(set(map(int, input().strip().split(" "))))
    # [max, ... , min] -> 0, ... , n
    runner_scores.sort(reverse=True)
    print(runner_scores[SECOND_PLACE])
