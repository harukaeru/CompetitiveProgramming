#!/usr/bin/env python3.8
import sys
sys.setrecursionlimit(300000)
N, Q = map(int, input().split())

L = {}
R = {}

for i in range(Q):
    q, *a = map(int, input().split())

    if q == 1:
        x, y = a
        L[x] = y
        R[y] = x
    elif q == 2:
        x, y = a
        del L[x]
        del R[y]
    elif q == 3:
        x, = a
        while R.get(x):
            x = R[x]

        ans = []
        while x:
            ans.append(x)
            x = L.get(x)
        print(len(ans), end=' ')
        print(' '.join(map(str, ans)))
        # elif len(l) == 1:
        #     print(len(l), end=' ')

