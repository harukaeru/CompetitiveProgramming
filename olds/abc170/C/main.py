#!/usr/bin/env python3.8
X, N = map(int, input().split())
if N == 0:
    print(X)
    exit()

*p, = map(int, input().split())

min_d = 9999999999
pos = 9999999999

for i in range(102, -2, -1):
    if i in p:
        continue
    d = abs(i - X)
    if min_d >= d:
        min_d = d
        pos = i

print(pos)
