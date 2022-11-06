#!/usr/bin/env python3.8
from collections import deque, defaultdict

MOD = 1000000007  # type: int
MAX = 999999999999

N, M = map(int, input().split())
G = {}
for i in range(N):
    G[i] = []

for i in range(M):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1

    G[a].append(b)
    G[b].append(a)

q = deque()
q.append(0)
distances = [None] * N
distances[0] = 0

counters = [0] * N
counters[0] = 1

while len(q) > 0:
    n = q.popleft()
    # print('N', n + 1)

    for next_node in G[n]:
        if distances[next_node] is None:
            distances[next_node] = distances[n] + 1
            counters[next_node] += counters[n]
            q.append(next_node)
        elif distances[next_node] == distances[n] + 1:
            counters[next_node] += counters[n]
            counters[next_node] %= MOD

print(counters[N - 1])
