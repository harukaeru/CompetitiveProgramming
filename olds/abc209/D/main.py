#!/usr/bin/env python3.8
from collections import defaultdict, deque
N, Q = map(int, input().split())

group_red = set()
group_blue = set()

edges = []
G = defaultdict(list)
for i in range(N - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    G[a].append(b)
    G[b].append(a)


q = deque()
q.append(0)
categories = [None] * N
categories[0] = 1

while len(q) > 0:
    n = q.popleft()

    for next_node in G[n]:
        if categories[next_node] is None:
            categories[next_node] = 3 - categories[n]
            q.append(next_node)

for i in range(Q):
    c, d = map(int, input().split())
    c, d = c - 1, d - 1
    if categories[c] == categories[d]:
        print('Town')
    else:
        print('Road')

# print(categories)
