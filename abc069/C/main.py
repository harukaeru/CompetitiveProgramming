#!/usr/bin/env python3.8
N = int(input())
A = list(map(int, input().split()))

c4 = 0
c2 = 0
c1 = 0
for i in range(N):
  a = A[i]
  if a % 4 == 0:
    c4 +=1
  elif a % 2 == 0:
    c2 += 1
  else:
    c1 += 1

# print(c1, c2, c4)
if c4 + 1 == c1 and N == c4 + c1:
  print('Yes')
elif c4 < c1:
  print('No')
else:
  print('Yes')
