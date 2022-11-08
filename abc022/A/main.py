#!/usr/bin/env python3.8
N, S, T = map(int, input().split())
W = int(input())

c = 0
if S <= W <= T:
  c += 1
for i in range(2, N + 1):
  a = int(input())
  W += a
  W = max(W, 1)
  if S <= W <= T:
    c += 1
print(c)