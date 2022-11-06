#!/usr/bin/env python3.8
N, M = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

A.reverse()
C.reverse()

B = []
# print('CI', C)
for i in range(M + 1):
  b = C[i] // A[0]
  B.append(b)
  for j in range(N + 1):
    C[i + j] -= A[j] * b
  # print(C)
# print('B', B)
B.reverse()
print(*B)