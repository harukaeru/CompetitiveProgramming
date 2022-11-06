#!/usr/bin/env python3.8
from queue import PriorityQueue

q = PriorityQueue()
c = 0

Q = int(input())

for i in range(Q):
    *query, = map(int, input().split())

    if query[0] == 1:
        q.put(query[1] - c)
    elif query[0] == 2:
        c += query[1]
    else:
        p1 = q.get()
        print(p1 + c)
