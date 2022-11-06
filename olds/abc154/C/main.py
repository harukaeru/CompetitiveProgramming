#!/usr/bin/env python3.8
N = int(input())
*A, = map(int, input().split())

if list(sorted(A)) == list(sorted(set(A))):
    print('YES')
else:
    print('NO')
