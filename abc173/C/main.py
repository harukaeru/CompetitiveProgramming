#!/usr/bin/env python3
H, W, K = map(int, input().split())

c = []
for i in range(H):
  c.append(input())

cnt = 0
for h in range(2 ** H):
  for w in range(2 ** W):
    black = 0
    for i in range(H):
      for j in range(W):
        if ((h >> i) & 1) == 0 and ((w >> j & 1)) == 0:
          if c[i][j] == '#':
            black += 1
    if black == K:
      cnt += 1
print(cnt)