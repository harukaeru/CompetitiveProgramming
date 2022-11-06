#!/usr/bin/env python3.8

N = int(input())
A = list(map(int, input().replace('\n', '').split()))

max1 = -1
max1_i = -1
max2 = -1
max2_i = -1

for i, a in enumerate(A):
    if (max1 < a):
        max2 = max1
        max2_i = max1_i

        max1 = a
        max1_i = i
    elif (max2 < a):
        max2 = a
        max2_i = i

print(max2_i + 1)
