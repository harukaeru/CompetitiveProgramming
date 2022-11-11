#!/usr/bin/env python3.8
N = int(input())
A = []
for i in range(N):
  a = int(input())
  A.append(a - 1)

nex = 0
seen = set()
cnt = 0
while nex != 1:
  cnt += 1
  seen.add(nex)
  nex = A[nex]
  if nex == 1:
    print(cnt)
    exit()
  if nex in seen:
    print(-1)
    exit()