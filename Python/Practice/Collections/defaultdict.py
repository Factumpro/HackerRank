#!/usr/div/env python3
# -*- coding: UTF-8 -*-

from collections import defaultdict

if __name__ == '__main__':
    words_group = defaultdict(list)
    n_size, m_size = map(int, input().split())
    [words_group[input()].append(str(i)) for i in range(1, n_size + 1)]
    for _ in range(m_size):
        item = input()
        if item in words_group:
            print(*words_group[item])
        else:
            print(-1)
