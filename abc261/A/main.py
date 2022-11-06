#!/usr/bin/env python3.8
l1, r1, l2, r2 = map(int, input().split())

ma = max(l1, l2)
mi = min(r1, r2)

if mi >= ma:
  print(mi - ma)
else:
  print(0)