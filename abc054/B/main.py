#!/usr/bin/env python3.8
N, M = map(int, input().split())
A = []
for i in range(N):
  a = input()
  A.append(a)

B = []
for i in range(M):
  b = input()
  B.append(b)

# Aを[0,N-M]の範囲で探索する
for i in range(N - M + 1):
  for j in range(N - M + 1):
    is_inside = True
    # Bの値と照合していき、不一致があればFalse
    for di in range(M):
      for dj in range(M):
        if B[di][dj] != A[i + di][j + dj]:
          is_inside = False
    if is_inside:
      print('Yes')
      exit()
print('No')