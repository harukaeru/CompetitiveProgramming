#!/usr/bin/env python3.8
N, M = map(int, input().split())
S = []
for i in range(N):
  s = input()
  S.append(s)

cnt = 0
for i in range(N):
  for j in range(N):
    if i == j:
      continue
    ok = True
    for k in range(M):
      if S[i][k] == 'x' and S[j][k] == 'x':
        ok = False
    if ok:
      cnt += 1
print(cnt // 2)