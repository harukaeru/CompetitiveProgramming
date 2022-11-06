#!/usr/bin/env python3.8
from collections import defaultdict, deque
N, M = map(int, input().split())

G = defaultdict(list)

for i in range(M):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    G[a].append(b)


def find(s):
    q = deque()
    q.append(s)
    seens = [False] * N
    seens[s] = True

    while len(q) > 0:
        n = q.popleft()

        for next_node in G[n]:
            if not seens[next_node]:
                seens[next_node] = True
                q.append(next_node)
    return seens.count(True)

t = 0
for i in range(N):
    t += find(i)
print(t)
