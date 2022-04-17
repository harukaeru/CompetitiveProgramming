#!/usr/bin/env python3

YES = "Yes"  # type: str
NO = "No"  # type: str

from collections import defaultdict
G = defaultdict(set)

N = int(input())
for i in range(N- 1):
    a, b = map(int, input().split())
    G[a].add(b)
    G[b].add(a)

for k, v in G.items():
    if len(v) == N - 1:
        print(YES)
        exit()

print(NO)
