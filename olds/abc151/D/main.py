#!/usr/bin/env python3.8
from collections import defaultdict, deque
H, W = map(int, input().split())

HW = []
for i in range(H):
    ww = list(input())
    HW.append(ww)

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def find(s):
    distances = dict()

    q = deque()
    q.append(s)
    distances[s] = 0

    while len(q) > 0:
        n = q.popleft()

        for d in directions:
            next_pos_0 = n[0] + d[0]
            next_pos_1 = n[1] + d[1]
            next_pos = (next_pos_0, next_pos_1)
            if distances.get(next_pos) is None:
                if next_pos_0 < 0 or next_pos_0 >= H:
                    continue

                if next_pos_1 < 0 or next_pos_1 >= W:
                    continue

                if HW[next_pos_0][next_pos_1] == '#':
                    continue

                distances[next_pos] = distances[n] + 1
                q.append(next_pos)
    # print('dis', distances)
    return max(distances.values())

points = [(i, j) for i in range(H) for j in range(W)]

max_d = 0
for p in points:
    if HW[p[0]][p[1]] == '#':
        continue

    # print('p', p, find(p))
    max_d = max(max_d, find(p))

print(max_d)
