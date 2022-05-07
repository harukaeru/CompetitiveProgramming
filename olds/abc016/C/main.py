#!/usr/bin/env python3
from collections import defaultdict, deque

N, M = map(int, input().split())
G = defaultdict(list)
for i in range(M):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    G[a].append(b)
    G[b].append(a)

def find(s):
    distances = [None] * N
    distances[s] = 0
    q = deque()
    q.append(s)

    while len(q) > 0:
        n = q.popleft()

        for next_node in G[n]:
            if distances[next_node] is None:
                distances[next_node] = distances[n] + 1
                q.append(next_node)

    return distances.count(2)

for i in range(N):
    print(find(i))

