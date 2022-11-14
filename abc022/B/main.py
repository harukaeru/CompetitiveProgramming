#!/usr/bin/env python3.8
N = int(input())
A = []
for i in range(N):
  A.append(int(input()))

cnt = 0
C = set()
for a in A:
  if a in C:
    cnt += 1
  C.add(a)
print(cnt)