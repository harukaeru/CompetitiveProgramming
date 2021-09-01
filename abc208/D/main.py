#!/usr/bin/env python3
from collections import deque

# import cProfile, pstats, io
# from pstats import SortKey
# pr = cProfile.Profile()
# pr.enable()

N, M = map(int, input().split())

INF = 999999999999
G = {}
C = {}
for j in range(1, N + 1):
    G[j] = []

dist = [
    [0 if i == j else INF for j in range(N)]
    for i in range(N)
]

for i in range(M):
    A_i, B_i, C_i = map(int, input().split())
    A_i -= 1
    B_i -= 1
    dist[A_i][B_i] = C_i

ans = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    for i in range(N):
        for j in range(N):
            if dist[i][j] < INF:
                ans += dist[i][j]
print(ans)
