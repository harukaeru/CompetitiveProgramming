#!/usr/bin/env python3.8
import math

N = int(input())

s = 0
for i in range(1, N + 1):
    s += i
    # print('s', s, N)
    if N <= s:
        print(i)
        exit()

