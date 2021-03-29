#!/usr/bin/env python3

if __name__ == '__main__':
    """example
    >>> 1, 1, 1, 2
    '[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]'
    """
    x, y, z, n = (int(input()) for _ in range(4))
    print(
         [[a, b, c] for a in range(x+1) for b in range(y+1) for c in range(z+1)
          if (a + b + c != n)]
          )
