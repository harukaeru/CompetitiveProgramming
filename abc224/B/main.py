#!/usr/bin/env python3
H, W = map(int, input().split())
a = []
for i in range(H):
  _a = list(map(int, input().split()))
  a.append(_a)


for i1 in range(H):
  for j1 in range(W):
    a_i1_j1 = a[i1][j1]
    for i2 in range(i1 + 1, H):
      for j2 in range(j1 + 1, W):
        if not (a_i1_j1 + a[i2][j2] <= a[i2][j1] + a[i1][j2]):
          print("No")
          exit()
print("Yes")