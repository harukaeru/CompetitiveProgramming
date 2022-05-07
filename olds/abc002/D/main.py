#!/usr/bin/env python3
import sys
import itertools

N, M = map(int, input().split())
xy = {}
for __ in range(M):
    x_i, y_i = map(int, input().split())
    xy[(x_i, y_i)] = True


m = -1
for b in range(2 ** N):
    group = []
    for i in range(N):
        if (b >> i) & 1:
            group.append(i + 1)

    is_found = True
    for c in itertools.combinations(group, 2):
        cx, cy = c
        if cy < cx:
            cx, cy = cy, cx
        if not xy.get((cx, cy)):
            is_found = False
    if not is_found:
        continue

    length = len(group)
    m = max(m, length)

print(m)
