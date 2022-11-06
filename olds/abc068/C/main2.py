#!/usr/bin/env python3.8
from collections import defaultdict, deque

YES = "POSSIBLE"  # type: str
NO = "IMPOSSIBLE"  # type: str

N, M = map(int, input().split())
G = defaultdict(list)

for i in range(M):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    G[a].append(b)
    G[b].append(a)


q = deque()
q.append(0)

distances = [None] * N
distances[0] = 0

while len(q) > 0:
    n = q.popleft()

    for next_node in G[n]:
        if distances[next_node] is None:
            distances[next_node] = distances[n] + 1
            q.append(next_node)


ok = distances[N - 1] == 2
if ok:
    print(YES)
else:
    print(NO)
