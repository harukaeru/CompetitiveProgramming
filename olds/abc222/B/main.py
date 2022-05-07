#!/usr/bin/env python3
N, P = map(int, input().split())
*a, = map(int, input().split())

s = 0
for ai in a:
    if ai < P:
        s += 1
print(s)
