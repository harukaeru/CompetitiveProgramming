#!/usr/bin/env python3.8
N, x = map(int, input().split())
*a, = map(int, input().split())

a.sort()

count = 0
for aa in a:
    x -= aa
    if x >= 0:
        count += 1
if x > 0:
    count -= 1
print(count)
