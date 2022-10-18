#!/usr/bin/env python3
from collections import defaultdict

N, M = map(int, input().split())
G = defaultdict(list)

counter = [0] * N
for i in range(M):
    a, b = map(int, input().split())
    if a > b:
        counter[a - 1] += 1
    if b > a:
        counter[b - 1] += 1

print(sum([1 for c in counter if c == 1]))