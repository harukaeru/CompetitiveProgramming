#!/usr/bin/env python3
H, W, X, Y = map(int, input().split())
S = []
for i in range(H):
  S.append(input())


x, y = X - 1, Y - 1

def p(i, j):
  pass
  # print('(', i + 1, ',', j + 1, ')')

cnt = 0
for i in range(x, -1, -1):
  if '#' == S[i][y]:
    break
  p(i, y)
  cnt += 1
for i in range(x, H):
  if '#' == S[i][y]:
    break
  p(i, y)
  cnt += 1

for i in range(y, -1, -1):
  if '#' == S[x][i]:
    break
  p(x, i)
  cnt += 1
for i in range(y, W):
  if '#' == S[x][i]:
    break
  p(x, i)
  cnt += 1

print(cnt - 3)