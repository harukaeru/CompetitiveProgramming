#!/usr/bin/env python3.8
T = int(input())
A = []
S = []
for i in range(T):
  a, s = map(int, input().split())
  A.append(a)
  S.append(s)

for i in range(T):
  a = A[i]
  s = S[i]
  if a <= s and (a & (s - a)) == a:
    print('Yes')
  else:
    print('No')