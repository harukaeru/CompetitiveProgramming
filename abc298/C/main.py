#!/usr/bin/env python3.8
N = int(input())
Q = int(input())

P = [set() for i in range(2 * (10 ** 5))]
A = [[] for i in range(N)]
for i in range(Q):
  x = list(map(int, input().split()))
  if x[0] == 1:
    i, j = x[1:]
    A[j - 1].append(i)
    P[i - 1].add(j)
  if x[0] == 2:
    j = x[1]
    A[j - 1].sort()
    print(*A[j - 1])
  if x[0] == 3:
    i = x[1]
    pi = list(P[i - 1])
    pi.sort()
    print(*pi)