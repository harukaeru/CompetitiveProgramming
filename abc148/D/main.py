#!/usr/bin/env python3.8
N = int(input())
A = list(map(int, input().split()))

t = 1
cnt = 0
for i in range(N):
  a = A[i]
  if a == t:
    cnt += 1
    t += 1

if cnt == 0:
  print(-1)
  exit()

print(N - cnt)