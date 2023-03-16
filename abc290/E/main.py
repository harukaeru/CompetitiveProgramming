#!/usr/bin/env python3.8
N=int(input())
A=list(map(int,input().split()))

C = [0] * (N + 1)
for a in A:
  C[a] += 1

print('A', A)
ans = 0
for i in range((N + 1) // 2):
  l = A[i]
  print('~i', ~i)
  r = A[~i]
  print(l)
  print(r)
  print('----')

  ans += (N - 2 * i - C[l]) * (i + 1)
  ans += (N - 2 * i - C[r]) * (i + 1)
  if l != r:
    ans -= i + 1

  C[l] -= 1
  C[r] -= 1
print(ans)