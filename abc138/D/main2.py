#!/usr/bin/env python3
N, Q = map(int, input().split())

G = {}
for v in range(N):
    G[v] = []

for i in range(N - 1):
    a_i, b_i = map(int, input().split())
    a_i, b_i = a_i - 1, b_i - 1
    G[a_i].append(b_i)
    G[b_i].append(a_i)

points_dict = {}
for j in range(Q):
    p_j, x_j = map(int, input().split())
    p_j = p_j - 1
    if points_dict.get(p_j) is None:
        points_dict[p_j] = 0
    points_dict[p_j] += x_j

counters = [0] * N
seens = [False] * N

stacks = []
stacks.append(0)
parents = []
while len(stacks):
    v = stacks.pop()

    seens[v] = True

    x = points_dict.get(v, 0)
    counters[v] += x

    for next_v in G[v]:
        if seens[next_v]:
            continue

        stacks.append(next_v)
        counters[next_v] += counters[v]

print(' '.join(map(str, counters)))
