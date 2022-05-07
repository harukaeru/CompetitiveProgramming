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

counters = [0] * N
for j in range(Q):
    p_j, x_j = map(int, input().split())
    p_j = p_j - 1
    counters[p_j] += x_j

seens = [False] * N

stacks = []
stacks.append((0, None))
while len(stacks):
    v, parent = stacks.pop()

    # seens[v] = True

    for next_v in G[v]:
        if next_v == parent:
            continue

        stacks.append((next_v, v))
        counters[next_v] += counters[v]

print(' '.join(map(str, counters)))
