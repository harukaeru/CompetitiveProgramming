#!/usr/bin/env python3
N = int(input())

A = []
for i in range(N):
  a = input()
  A.append(a)

for i in range(N):
  for j in range(N):
    # print('i,j', i,j )
    if i == j:
      continue
    if A[i][j] == 'W':
      if A[j][i] != 'L':
        print('incorrect')
        exit()
    if A[i][j] == 'L':
      if A[j][i] != 'W':
        print('incorrect')
        exit()
    if A[i][j] == 'D':
      if A[j][i] != 'D':
        print('incorrect')
        exit()
print('correct')