#!/usr/bin/env python3.8
# from collections import deque
import heapq
a, b, x, y =map(int, input().split())

class Node:
    def __init__(self, label):
        self.label = label
        self.cost = 99999999999

G = {}
INF = 99999999999
maxA = 100
maxB = 100
C = {}

for a_floor in range(1, maxA + 1):
    current_floor = 'a' + str(a_floor)
    C[current_floor] = INF
    if not G.get(current_floor):
        G[current_floor] = []

    if a_floor != maxA:
        # 最上階じゃないとき
        a_upper_floor = 'a' + str(a_floor + 1)
        G[current_floor].append([a_upper_floor, y])

    if a_floor != 1:
        # 下の階があるとき
        a_lower_floor = 'a' + str(a_floor - 1)
        b_lower_floor = 'b' + str(a_floor - 1)
        G[current_floor].append([a_lower_floor, y])
        G[current_floor].append([b_lower_floor, x])
    b_same_floor = 'b' + str(a_floor)
    G[current_floor].append([b_same_floor, x])

for b_floor in range(1, maxB + 1):
    current_floor = 'b' + str(b_floor)
    C[current_floor] = INF
    if not G.get(current_floor):
        G[current_floor] = []

    if b_floor != maxA:
        # 最上階じゃないとき
        b_upper_floor = 'b' + str(b_floor + 1)
        a_upper_floor = 'a' + str(b_floor + 1)
        G[current_floor].append([b_upper_floor, y])
        G[current_floor].append([a_upper_floor, x])

    if b_floor != 1:
        # 下の階があるとき
        b_lower_floor = 'b' + str(b_floor - 1)
        G[current_floor].append([b_lower_floor, y])

    a_same_floor = 'a' + str(b_floor)
    G[current_floor].append([a_same_floor, x])

# from pprint import pprint
# pprint(G)

q = []
heapq.heapify(q)
start = 'a' + str(a)
end = 'b' + str(b)
heapq.heappush(q, (0, start))
C[start] = 0

done_nodes = set()

while len(q) > 0:
    current_cost, n = heapq.heappop(q)

    # current_cost = C[n]
    done_nodes.add(n)

    if n == end:
        print(C[n])
        exit()

    for next_n, path_cost in G[n]:
        if next_n in done_nodes:
            continue

        C[next_n] = min(C[next_n], current_cost + path_cost)

        heapq.heappush(q, (C[next_n], next_n))
    # print('q', q)

    # min_nname = None
    # min_ncost = 99999999999999999
    # for nname, ncost in C.items():
    #     if nname in done_nodes:
    #         continue
    #     if ncost < min_ncost:
    #         min_nname = nname
    #         min_ncost = ncost
    # q.append(min_nname)
