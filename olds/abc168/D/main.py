#!/usr/bin/env python3.8
from collections import defaultdict, deque

G = defaultdict(list)
N, M = map(int, input().split())
for i in range(M):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    G[a].append(b)
    G[b].append(a)

befores = [None] * N

q = deque()
q.append(0)

while len(q) > 0:
    n = q.popleft()

    for next_node in G[n]:
        if befores[next_node] is None:
            befores[next_node] = n
            q.append(next_node)


# print('befores', befores)

for i in befores[1:]:
    if i is None:
        print('No')
        exit()

print('Yes')
for i in befores[1:]:
    print(i + 1)
