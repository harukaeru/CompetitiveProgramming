#!/usr/bin/env python3.8
N = input()
A = list(map(int, N))
A.reverse()

ans = 0
for i in range(len(A)):
  if A[i] % 2 == 1:
    ans += A[i] % 2 * (2 ** i)
print(ans)