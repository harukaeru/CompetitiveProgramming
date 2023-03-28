#!/usr/bin/env python3.8
N,K=map(int, input().split())
T = []
for i in range(N):
  ts = list(map(int, input().split()))
  T.append(ts)

for i in range(K ** N):
  k = i
  p = None
  for j in range(N):
    if p is None:
      p = T[j][k % K]
    else:
      p ^= T[j][k % K]
    k //= K
  if p == 0:
    print('Found')
    exit()
print('Nothing')
