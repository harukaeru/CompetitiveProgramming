#!/usr/bin/env python3.8
N, K = map(int, input().split())

def k(n):
  if (n % 200 == 0):
    return n // 200
  else:
    return int(str(n) + '200')

for i in range(K):
  N = k(N)
  # print('N', N)

print(N)