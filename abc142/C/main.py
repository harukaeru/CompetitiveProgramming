#!/usr/bin/env python3.8
N = int(input())
A = list(map(int, input().split()))

revs = [None] * N
for i in range(N):
  id = A[i] - 1
  revs[id] = i + 1

print(' '.join(map(str, revs)))