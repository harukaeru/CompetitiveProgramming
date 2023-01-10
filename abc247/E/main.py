#!/usr/bin/env python3.8
N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

separator = []
for i in range(N):
  if A[i] < Y or A[i] > X:
    separator.append(i)

def check(B):
  ans = 0

  l, r = 0, 0
  x, y = 0, 0
  while l < len(B):
    while r < len(B) and (x == 0 or y == 0):
      if B[r] == X:
        x += 1
      if B[r] == Y:
        y += 1
      r += 1
  
    if x > 0 and y > 0:
      # 残りは全部満たす
      ans += len(B) + 1 - r

    if B[l] == X:
      x -= 1
    if B[l] == Y:
      y -= 1
    l += 1

  return ans


l = 0
r = separator[0] if separator else N

tot = check(A[l:r])

for i in range(len(separator)):
  if i + 1 == len(separator):
    l, r = r + 1, N
  else:
    l, r = r + 1, separator[i + 1]
  tot += check(A[l:r])
print(tot)

