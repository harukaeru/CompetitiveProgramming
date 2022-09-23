#!/usr/bin/env python3
N, K, X = map(int, input().split())
A = list(map(int, input().split()))

C = []
R = []
for a in A:
  c = a // X
  r = a % X
  C.append(c)
  R.append(r)

R.sort()
R.reverse()

tot = sum(A)
tot -= min(K, sum(C)) * X

rest = max(K - sum(C), 0)
tot -= sum(R[:rest])
print(tot)