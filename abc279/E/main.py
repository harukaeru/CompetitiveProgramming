#!/usr/bin/env python3.8
N, M = map(int, input().split())
A = list(map(int, input().split()))

B = list(range(0, N + 1))

for a in A:
  B[a], B[a + 1] = B[a+1],B[a]

pos = [None] * (N + 1)
for i in range(1, N+1):
  pos[B[i]] = i

B = list(range(0, N + 1))

for a in A:
  if B[a] == 1:
    print(pos[B[a + 1]])
  elif B[a + 1] == 1:
    print(pos[B[a]])
  else:
    print(pos[1])
  B[a], B[a + 1] = B[a+1],B[a]