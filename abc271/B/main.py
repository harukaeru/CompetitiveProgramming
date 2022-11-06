#!/usr/bin/env python3.8
N, Q = map(int, input().split())

Ls = []
A = []
for i in range(N):
  L, *a = map(int, input().split())
  Ls.append(L)
  A.append(a)

for i in range(Q):
  s, t = map(int, input().split())
  print(A[s - 1][t - 1])