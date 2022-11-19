#!/usr/bin/env python3.8
h, m = map(int, input().split())

for j in range(24 * 60):
  if m == 60:
    h = (h + 1) % 24
    m = 0

  H = '{0:02d}'.format(h)
  M = '{0:02d}'.format(m)

  wh = int(H[0] + M[0])
  wm = int(H[1] + M[1])
  if 0 <= wh <= 23 and 0 <= wm <= 59:
    print(h, m)
    exit()
  m += 1
