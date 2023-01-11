#!/usr/bin/env python3.8
N = int(input())
A = list(map(int, input().split()))

tot = 0
for r in range(N):
  if r == 0 or A[r-1] >= A[r]:
    l = r
  tot += r - l + 1
print(tot)