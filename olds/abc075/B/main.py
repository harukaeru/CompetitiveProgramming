#!/usr/bin/env python3.8
H, W = map(int, input().split())
S = []
for __ in range(H):
    S.append(list(input()))

R = [
  [0 for j in range(W)]
  for i in range(H)
]

verticals = [+1, -1, 0]
horizontals = [+1, -1, 0]

for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            R[i][j] = '#'
            for v in verticals:
                for h in horizontals:
                    if (0 <= i + v < H) and (0 <= h + j < W) and (v != 0 or h != 0):
                        if R[i + v][h + j] != '#':
                            R[i + v][h + j] += 1

for i in range(H):
    for j in range(W):
        print(R[i][j], end='')
    print()
