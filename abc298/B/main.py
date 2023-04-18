#!/usr/bin/env python3.8
N = int(input())
A = []
for i in range(N):
  a = list(map(int, input().split()))
  A.append(a)

B = []
for i in range(N):
  b = list(map(int, input().split()))
  B.append(b)

def is_ok(x, y):
  for i in range(N):
    for j in range(N):
      if x[i][j] == 1:
        if y[i][j] == 0:
          return False
  return True

def rotate(A):
  R = []
  for i in range(N):
    R.append([None] * N)

  for i in range(N):
    for j in range(N):
      R[N+1-(j + 1) - 1][i] = A[i][j]
  return R

for i in range(4):
  A = rotate(A)
  
  if is_ok(A, B):
    print('Yes')
    exit()
print('No')