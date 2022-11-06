#!/usr/bin/env python3.8
N = int(input())
xy = []
for i in range(N):
  x, y = map(int, input().split())
  xy.append((x, y))

# xy.sort()
cnt = 0
total = 0
for i in range(N - 2):
  x_i, y_i = xy[i]
  for j in range(i + 1, N - 1):
    x_j, y_j = xy[j]
    dx1 = x_j - x_i
    dy1 = y_j - y_i

    for k in range(j + 1, N):
      total += 1
      x_k, y_k = xy[k]

      dx2 = x_k - x_i
      dy2 = y_k - y_i

      if dx1 * dy2 == dy1 * dx2:
        cnt += 1

print(total - cnt)