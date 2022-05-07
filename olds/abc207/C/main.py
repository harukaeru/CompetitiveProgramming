#!/usr/bin/env python3
N = int(input())
a = []
for __ in range(N):
    t, l, r = map(int, input().split())
    if t == 2:
        r -= 0.1
    elif t == 3:
        l += 0.1
    elif t == 4:
        l += 0.1
        r -= 0.1
    a.append((l, r))

comb = set()

def merge(x, y, i, j):
    max_l = max(x[0], y[0])
    min_r = min(x[1], y[1])
    if min_r - max_l < 0:
        return 0

    comb.add((i, j))

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        merge(a[i], a[j], i, j)
print(len(comb))
