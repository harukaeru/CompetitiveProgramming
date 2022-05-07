#!/usr/bin/env python3
N = int(input())

K = set()
for i in range(N):
    K.add(input())

if len(K) == N:
    print('No')
else:
    print('Yes')
