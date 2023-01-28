#!/usr/bin/env python3.8
N,M=map(int, input().split())
S = []
for i in range(N):
  S.append(input())

T = []
for i in range(M):
  T.append(input())


cnt = 0
for i in range(N):
  s = S[i]
  ok = False
  for j in range(M):
    t = T[j]
    if s.endswith(t):
      ok = True
      break
  if ok:
    cnt += 1
print(cnt)