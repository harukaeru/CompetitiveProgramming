#!/usr/bin/env python3.8
N, X, Y = map(int, input().split())

req = abs(X) + abs(Y)

if N < req:
  print('No')
  exit()

rest = N - req
if rest % 2 == 1:
  print('No')
else:
  print('Yes')