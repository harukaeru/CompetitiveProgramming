#!/usr/bin/env python3
# from pprint import pprint
from collections import deque
N = int(input())

A = [
    list(map(int, input().split())),
    list(map(int, input().split())),
]

S = [
    [0 for x in  range(N)],
    [0 for x in  range(N)],
]

que = deque()
que.append((0, 0))
S[0][0] += A[0][0]

while len(que) > 0:
    i, j = que.popleft()

    nexts = []
    if i == 0:
        nexts.append((i + 1, j))
    if j < N - 1:
        nexts.append((i, j + 1))

    # print('(', i, j, ')')
    # pprint(S[0])
    # pprint(S[1])

    for next_pos in nexts:
        next_i, next_j = next_pos

        S[next_i][next_j] = max(S[next_i][next_j], A[next_i][next_j] + S[i][j])
        que.append(next_pos)

print(S[-1][-1])
# pprint(S)
