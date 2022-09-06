#!/usr/bin/env python3
W, H, x, y = map(int, input().split())

g_0, g_1 = W / 2, H / 2

S = W * H / 2

if g_0 == x and g_1 == y:
  print(S, 1)
else:
  print(S, 0)