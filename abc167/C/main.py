#!/usr/bin/env python3
N, M, X = map(int, input().split())
C = []
A = []
for i in range(N):
  c, *a = list(map(int, input().split()))
  C.append(c)
  A.append(a)

BIG = 9999999999999999
min_money = BIG
for i in range(2 ** N + 1):
  k = i
  algos = [0] * M
  money = 0
  for j in range(N):
    chosen = k % 2 
    if chosen:
      money += C[j]
      for t in range(M):
        algos[t] += A[j][t]
    k //= 2
  
  if all([a >= X for a in algos]):
    min_money = min(min_money, money)

if min_money == BIG:
  print(-1)
else:
  print(min_money)