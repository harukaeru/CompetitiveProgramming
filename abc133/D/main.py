#!/usr/bin/env python3.8
N = int(input())
A = list(map(int, input().split()))

d = 0
for i in range(N - 1):
  if i % 2 == 0:
    d += 2 * A[i]
  else:
    d -= 2 * A[i]

x1 = (d + 2 * A[N - 1]) // 2
anses = [x1]
x = x1

for i in range(N - 1):
  a = A[i]
  x = 2 * a - x
  anses.append(x)
print(*anses)