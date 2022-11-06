#!/usr/bin/env python3.8
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

mons_cnt = 0
for i in range(N - 1, -1, -1):
  if B[i] >= A[i + 1]:
    B[i] -= A[i + 1]
    mons_cnt += A[i + 1]
    A[i + 1] = 0
  else:
    A[i + 1] -= B[i]
    mons_cnt += B[i]
    B[i] = 0

  if B[i] <= 0:
    continue

  if B[i] >= A[i]:
    B[i] -= A[i]
    mons_cnt += A[i]
    A[i] = 0
  else:
    A[i] -= B[i]
    mons_cnt += B[i]
    B[i] = 0

  # print('------------', i)
  # print('A', A)
  # print('B', B)
  # print('cnt', mons_cnt)
print(mons_cnt)