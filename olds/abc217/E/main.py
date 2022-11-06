#!/usr/bin/env python3.8
from collections import deque
from queue import PriorityQueue

Q = int(input())
A1 = deque()
A2 = PriorityQueue()
pointer = 0
for i in range(Q):
    *q, = map(int, input().split())

    if q[0] == 1:
        A1.append(q[1])
    elif q[0] == 2:
        if not A2.empty():
            print(A2.get())
        else:
            print(A1.popleft())
    else:
        while len(A1) > 0:
            A2.put(A1.popleft())
    # print(A)
