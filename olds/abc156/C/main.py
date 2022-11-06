#!/usr/bin/env python3.8
N = int(input())
*X, = map(int, input().split())

vitalities = []
for p in range(100):
    vitality = 0
    for i in X:
        vitality += (i - p) ** 2
    vitalities.append(vitality)

print(min(vitalities))
