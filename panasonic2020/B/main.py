#!/usr/bin/env python3.8
H, W = map(int, input().split())

if H == 1 or W == 1:
  print(1)
else:
  print((H * W + 1) // 2)