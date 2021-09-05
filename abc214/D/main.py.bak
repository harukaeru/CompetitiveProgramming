#!/usr/bin/env python3
from collections import deque

N = int(input())
INF = 9999999999

G = {}
C = {}

for i in range(N):
    G[i] = []
    C[i] = INF

for i in range(N - 1):
    *x, = map(int, input().split())
    u_i, v_i, w_i = x
    u_i = u_i - 1
    v_i = v_i - 1
    G[u_i].append(v_i)
    G[v_i].append(u_i)
    C[(u_i, v_i)] = w_i
    C[(v_i, u_i)] = w_i

def f(u, v):
    q = deque()
    q.append(u)
    costs = {}
    max_edge_costs = {}

    for i in range(N):
        costs[i] = INF
        max_edge_costs[i] = 0
    costs[u] = 0

    done_nodes = set()

    while len(q) > 0:
        n = q.popleft()
        done_nodes.add(n)

        if n == v:
            return max_edge_costs[v]

        if len(done_nodes) == N:
            raise Exception('WTF')


        for next_n in G[n]:
            if next_n in done_nodes:
                continue
            new_cost = costs[n] + C[(n, next_n)]
            if costs[next_n] >= new_cost:
                costs[next_n] = new_cost
                max_edge_costs[next_n] = max(max_edge_costs[next_n], C[(n, next_n)])
            # costs[next_n] = min(costs[next_n], costs[n] + C[(n, next_n)])

        min_cost = INF
        min_node = -1
        for nn in range(N):
            if nn in done_nodes:
                continue
            if min_cost >= costs[nn]:
                min_cost = costs[nn]
                min_node = nn
        if min_node != -1:
            q.append(min_node)


s = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        s += f(i, j)

print(s)
