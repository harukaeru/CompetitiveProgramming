#!/usr/bin/env python3
N, Q = map(int, input().split())
S = input()

lens = len(S)
first = 0

for i in range(Q):
  t, x = map(int, input().split())
  if t == 1:
    first -= x
    first %= lens

  if t == 2:
    si = (first + (x - 1) + lens) % lens
    print(S[si])