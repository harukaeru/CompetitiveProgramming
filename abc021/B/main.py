#!/usr/bin/env python3.8
N = int(input())
a, b = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

P = set([a, b])
for x in A:
  if x in P:
    print('NO')
    exit()
  P.add(x)

print('YES')