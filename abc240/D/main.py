#!/usr/bin/env python3.8
N = int(input())
A = list(map(int, input().split()))

S = []
tot = 0

for i in range(N):
  if len(S) == 0:
    tot += 1
    S.append([A[i], 1])
  elif S[-1][0] != A[i]:
    tot += 1
    S.append([A[i], 1])
  else:
    tot += 1
    S[-1][1] += 1
    if S[-1][1] == A[i]:
      tot -= A[i]
      S.pop()
  print(tot)