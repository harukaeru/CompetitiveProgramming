#!/usr/bin/env python3
from functools import cmp_to_key

N, M = map(int, input().split())
A = []
for i in range(N * 2):
    *a, = input()
    A.append(a)

def battle(x, y):
    if x == 'G' and y == 'C':
        return 'left'
    if x == 'G' and y == 'P':
        return 'right'
    if x == 'C' and y == 'P':
        return 'left'
    if x == 'C' and y == 'G':
        return 'right'
    if x == 'P' and y == 'G':
        return 'left'
    if x == 'P' and y == 'C':
        return 'right'
    return 'draw'

win_counts = [0] * (N * 2)

def round(L, r):
    # print('A', A)
    # print('r', r)
    # print('L', list(map(lambda a: a +1, L)))
    for i in range(0, len(L) - 1, 2):
        # print(A[L[i]])
        mean1 = A[L[i]][r]
        mean2 = A[L[i+1]][r]
        result = battle(mean1, mean2)
        if result == 'left':
            win_counts[L[i]] += 1
        elif result == 'right':
            win_counts[L[i + 1]] += 1

def howsort(a, b):
    if win_counts[a] > win_counts[b]:
        return -1
    elif win_counts[a] < win_counts[b]:
        return 1
    if a < b:
        return -1
    return 1

m = M
L = list(range(N * 2))
r = 0
# print('L', L)
# print('win_counts', win_counts)
while m > 0:
    round(L, r)
    # print('win_counts', win_counts)
    L.sort(key=cmp_to_key(howsort))
    r += 1
    m -= 1

for i in L:
    print(i+1)
