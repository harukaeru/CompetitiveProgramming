#!/usr/bin/env python3
N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

ans = []
for i in range(P, Q + 1):
  row = ['.'] * (S - R + 1)
  ans.append(row)

for x in range(P, Q + 1):
  for y in range(R, S + 1):
    vec = (x - A, y - B)
    if vec[0] != vec[1] and vec[0] != -vec[1]:
      continue

    ans[x - P][y - R] = '#'

for a in ans:
  print(''.join(a))