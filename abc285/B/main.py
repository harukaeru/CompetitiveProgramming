#!/usr/bin/env pypy3
N = int(input())
S = input()

S = ' ' + S

for i in range(1, N):
  m = 0
  for k in range(N):
    if k + i < N + 1:
      if S[k] != S[k + i]:
        m = max(m, k)
      else:
        break
  print(m)

