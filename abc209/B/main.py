#!/usr/bin/env python3
N, X = map(int, input().split())
*A, = map(int, input().split())

s = 0
for i, a in enumerate(A):
    if i % 2 != 0:
        s += a - 1
    else:
        s += a
if X >= s:
    print('Yes')
else:
    print('No')
