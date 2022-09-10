#!/usr/bin/env python3
N, M = map(int, input().split())
H = list(map(int, input().split()))

paths = {

} 
for i in range(M):
  a, b = map(int, input().split())
  a, b = a - 1, b - 1
  paths.setdefault(a, []).append(b)
  paths.setdefault(b, []).append(a)

cnt = 0
for i in range(N):
  greatest = True
  for p in paths.get(i, []):
    if H[i] <= H[p]:
      greatest = False
      break
  if greatest:
    cnt += 1

print(cnt)