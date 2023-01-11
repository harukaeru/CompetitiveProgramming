#!/usr/bin/env python3.8
N = int(input())
A = list(map(int, input().split()))

tot = 0
r = 0
for l in range(N):
  while r < N:
    if r == 0:
      break
    elif A[r - 1] >= A[r]:
      break
    r += 1

  tot += r - l + 1
  if l == r:
    r += 1
print(tot)