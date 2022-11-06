#!/usr/bin/env python3.8
N = int(input())
*A, = map(int, input().split())
X = int(input())

tot = sum(A)

group_idx = X // tot
rest = X % tot

# print('idx', group_idx)
# print('rest', rest)

if rest < 0:
    print(group_idx * N)
    exit()

for i, a in enumerate(A):
    rest -= a
    if rest < 0:
        print(group_idx * N + i + 1)
        exit()
