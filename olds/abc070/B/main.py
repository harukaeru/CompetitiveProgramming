#!/usr/bin/env python3.8
A, B, C, D = map(int, input().split())

maxBD = max(B, D)
a = [0] * (maxBD + 1)
a[A] += 1
a[B] += -1
a[C] += 1
a[D] += -1

for i in range(0, len(a) - 1):
    a[i + 1] += a[i]

print(a.count(2))
