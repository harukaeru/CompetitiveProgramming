#!/usr/bin/env python3
from collections import defaultdict

N, M = map(int, input().split())
G = defaultdict(list)

for i in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

cnt = 0
for i in range(1, N + 1):
    if len([j for j in G[i] if j < i]) == 1:
        cnt += 1
print(cnt)