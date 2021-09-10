#!/usr/bin/env python3
from collections import defaultdict, deque

YES = "POSSIBLE"  # type: str
NO = "IMPOSSIBLE"  # type: str

N, M = map(int, input().split())
edges = set()

for i in range(M):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    edges.add((a, b))
    edges.add((b, a))


for i in range(N):
    if (0, i) in edges and (i, N - 1) in edges:
        print(YES)
        exit()
print(NO)
