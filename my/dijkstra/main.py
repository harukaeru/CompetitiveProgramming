"""
6 9
0 1 3
1 2 4
0 2 5
1 3 12
2 4 4
4 3 7
4 5 8
3 5 2
2 3 9
"""
from collections import deque

INF = 999999999999
N, M = map(int, input().split())

G = {}
edge_costs = {}
for __ in range(M):
    v0, v1, cost = map(int, input().split())
    if not G.get(v0):
        G[v0] = []
    G[v0].append(v1)

    edge_costs[(v0, v1)] = cost


q = deque()
done_nodes = set()
node_costs = {
    i: INF for i in range(N)
}

q.append(0)
node_costs[0] = 0

while len(q) > 0:
    v = q.popleft()
    done_nodes.add(v)

    if v == N - 1:
        print(node_costs[v])
        exit()

    min_cost = INF
    node_idx = None
    for next_v in G[v]:
        if next_v in done_nodes:
            continue
        node_costs[next_v] = min(node_costs[next_v], edge_costs[(v, next_v)] + node_costs[v])

    for i in range(N):
        if i in done_nodes:
            continue
        if min_cost >= node_costs[i]:
            min_cost = node_costs[i]
            node_idx = i
    q.append(node_idx)
