#!/usr/bin/env python3.8
N = int(input())
A = list(map(int, input().split()))

anses = [None] * N
for i in range(N, 0, -1):
  if i == N:
    anses[i-1] = A[i-1]
  else:
    prev = 0
    for j in range(2 * i, N + 1, i):
      prev += anses[j - 1]
    prev %= 2
    if prev == A[i - 1]:
      anses[i - 1] = 0
    else:
      anses[i - 1] = 1

panses = []
for i, a in enumerate(anses, 1):
  if a == 1:
    panses.append(i)
print(len(panses))
if panses:
  print(*panses)