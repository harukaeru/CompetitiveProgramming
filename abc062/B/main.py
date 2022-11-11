#!/usr/bin/env python3.8
H, W = map(int, input().split())
S = []
for i in range(H):
  S.append(input())

O = []
for i in range(H + 2):
  if i == 0 or i == H + 1:
    O.append('#' * (W + 2))
  else:
    O.append('#' + S[i - 1] + '#')

for o in O:
  print(o)
