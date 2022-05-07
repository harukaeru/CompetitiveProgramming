#!/usr/bin/env python3
# import sys
# sys.setrecursionlimit(30000)

from collections import defaultdict

N, M = map(int, input().split())
G = defaultdict(list)
indeg_counters = [0] * (N)
for i in range(M):
    A, B = map(int, input().split())
    G[A].append(B)
    indeg_counters[B - 1] += 1

S = []

# from pprint import pprint

# pprint(G)

objectives = set()
# print('counters', indeg_counters)


# for i, c in enumerate(indeg_counters):
done_set = set()
i = 0
det = 0
while i < N:
    c = indeg_counters[i]
    n = i + 1
    if c == 0 and not n in done_set:
        done_set.add(n)
        S.append(n)
        if G.get(n):
            for l in G[n]:
                indeg_counters[l - 1] -= 1
        det += 1
        i = 0
        if det == N:
            break
    else:
        i += 1

if not S:
    print(-1)
else:
    print(' '.join(map(str, S)))
