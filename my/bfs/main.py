from pprint import pprint
from collections import deque

N, M = map(int, input().split())

G = {}
for i in range(N):
    G[i] = []

for __ in range(M):
    v_i, v_j = map(int, input().split())
    G[v_i].append(v_j)
    G[v_j].append(v_i)

pprint(G)

distances = [-1] * N
que = deque()

def bfs(G, v, nest):
    # global order
    seens[v] = True

    for next_v in G[v]:
        if seens[next_v]:
            continue

        print(' ' * nest * 2, next_v, 'o=>', first_orders[v], last_orders[v])
        bfs(G, next_v, nest + 1)

    # order += 1
    # last_orders[v] = order

distances[0] = 0
que.append(0)
while que:
    v = que.popleft()

    # print('G[v]', G[v])
    for next_v in G[v]:
        if distances[next_v] != -1:
            continue

        distances[next_v] = distances[v] + 1
        print(' ' * distances[next_v] * 2, next_v)
        que.append(next_v)
