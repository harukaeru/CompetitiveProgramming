#!/usr/bin/env python3.8
N, K = map(int, input().split())

if K % 2 != 0:
  cnt = 0
  for i in range(1, N + 1):
    if i % K == 0:
      cnt += 1
  print(cnt ** 3)
  exit()

cnt = 0
for i in range(1, N + 1):
  if i % K == 0:
    cnt += 1
cnt = cnt ** 3

r_cnt = 0
half = K // 2
for i in range(1, N + 1):
  if i % K == half:
    r_cnt += 1
print(cnt + r_cnt ** 3)