#!/usr/bin/env python3.8
from bisect import bisect_left


T = int(input())
for i in range(T):
  N = int(input())
  SS = input()

  # print('------')
  # print(S, '->', end=' ')

  if SS == '110' or SS == '011':
    print(-1)
    continue
  S = list(SS)

  c = 0
  prev = None
  adjacent = False
  for j in range(N):
    if S[j] == '1':
      c += 1

      if prev is None:
        prev = j
      else:
        if prev + 1 == j:
          adjacent = True

  if N == 4 and SS == '0110':
    print(3)
    continue

  # print('c', c)
  if c % 2 == 0:
    if c == 2 and adjacent:
      print(c // 2 + 1)
    else:
      print(c // 2)
  else:
    print(-1)