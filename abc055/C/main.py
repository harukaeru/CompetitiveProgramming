#!/usr/bin/env python3.8
N, M = map(int, input().split())

if N * 2 >= M:
  print(M // 2)
  exit()

cnt = N
M = M - N * 2
M //= 4
cnt += M
print(cnt)