#!/usr/bin/env python3


def meanMark(query_scores):
    return sum(query_scores)/len(query_scores)

if __name__ == '__main__':
    students = {}
    for _ in range(int(input())):
        data = input().split()
        name, scores = data[0], data[1:]
        scores = list(map(float, scores))
        students[name] = scores
    query_name = input()
    query_scores = students[query_name]
    # print(format(meanMark(query_scores), ".2f"))
    print('{:0.2f}'.format(meanMark(query_scores)))
