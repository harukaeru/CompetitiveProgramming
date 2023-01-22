#!/usr/bin/env python3.8
N = int(input())
A = []
B = []
for i in range(N):
  a = list(map(int, input().split()))
  b = a[:]
  A.append(a)
  B.append(b)

via = []
for i in range(N):
  d = [i] * N
  via.append(d)

for k in range(N):
  for i in range(N):
    for j in range(N):
      if i == k or k == j:
        continue
      if A[i][j] >= B[i][k] + B[k][j]:
        via[i][j] = k
        B[i][j] = min(B[i][j], B[i][k] + B[k][j])

# for v in via:
#   print(v)

ans = 0
for i in range(N):
  for j in range(N):
    if A[i][j] != B[i][j]:
      print('-1')
      exit()
    if i == via[i][j]:
      ans += B[i][j]
print(ans // 2)
