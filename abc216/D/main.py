#!/usr/bin/env python3
from collections import deque
from copy import deepcopy
N, M = map(int, input().split())

T = {}
for i in range(M):
    k = int(input())
    *a_i, = input().split()
    T[i] = deque(a_i)

# from pprint import pprint
# pprint(T)

counters = {
    str(i): [] for i in range(1, N + 1)
}

next_pop_queue = deque([])
# O(M)
for k, a_i in T.items():
    if not a_i:
        continue
    top_v = a_i[0]
    counters[top_v].append(k)
    if len(counters[top_v]) == 2:
        next_pop_queue.append(top_v)

while len(next_pop_queue) > 0:
    top_v = next_pop_queue.popleft()

    for t in counters[top_v]:
        cylinder = T[t]
        popped = cylinder.popleft()
        if len(cylinder) != 0:
            counters[cylinder[0]].append(t)
            if len(counters[cylinder[0]]) == 2:
                next_pop_queue.append(cylinder[0])

# from pprint import pprint
# pprint(T)
for ts in T.values():
    if len(ts) != 0:
        print('No')
        exit()

print('Yes')
# pprint(exist_keys)
