from pprint import pprint

N, M = map(int, input().split())

G = {}
for i in range(N):
    G[i] = []

for __ in range(M):
    v_i, v_j = map(int, input().split())
    G[v_i].append(v_j)
    G[v_j].append(v_i)

pprint(G)

seens = [False] * N
first_orders = [0] * N
last_orders = [0] * N

order = 0

def dfs(G, v, nest):
    global order
    seens[v] = True

    order += 1
    first_orders[v] = order

    for next_v in G[v]:
        if seens[next_v]:
            continue

        print(' ' * nest * 2, next_v, 'o=>', first_orders[v], last_orders[v])
        dfs(G, next_v, nest + 1)

    order += 1
    last_orders[v] = order


dfs(G, 0, 0)
orders_list = [None] * 2 * M
for i, o in enumerate(first_orders):
    orders_list[o] = i
for i, o in enumerate(last_orders):
    orders_list[o] = i
print(orders_list)
pprint(first_orders)
pprint(last_orders)
