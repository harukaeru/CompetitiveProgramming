#!/usr/bin/env python3.8
N = int(input())
*A, = map(int, input().split())

maximum = 0
count = 0
for i, a in enumerate(A):
    if a > maximum:
        maximum = a
    elif a < maximum:
        count += maximum - a
print(count)
