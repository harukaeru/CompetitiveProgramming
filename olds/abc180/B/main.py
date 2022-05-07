#!/usr/bin/env python3
import math

N = int(input())
*x, = map(int, input().split())

s = 0
s2 = 0
s3 = -99999999999999
for i in x:
    s += abs(i)
    s2 += abs(i) * abs(i)
    s3 = max(s3, abs(i))

print(s)
print(math.sqrt(s2))
print(s3)
