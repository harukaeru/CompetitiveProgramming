#!/usr/bin/env python3.8
R,C=map(int, input().split())
B = []
for i in range(R):
  A = list(input())
  B.append(A)

for i in range(R):
  for j in range(C):
    if B[i][j] != '.' and B[i][j] != '#':
      cnt = int(B[i][j])
      for l in range(-cnt, cnt + 1):
        for r in range(-cnt, cnt + 1):
          if abs(l) + abs(r) > cnt:
            continue
          if i + l < 0 or i + l > R - 1:
            continue
          if j + r < 0 or j + r > C - 1:
            continue

          if B[i + l][j + r] == '#':
            B[i + l][j + r] = '.'
      B[i][j] = '.'
    

for b in B:
  print(''.join(b))

