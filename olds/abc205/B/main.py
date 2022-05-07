#!/usr/bin/env python3
N = int(input())
*A, = map(int, input().split())


s = sorted(A)
t = list(range(1, N + 1))

if s == t:
    print('Yes')
else:
    print('No')
