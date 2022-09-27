#!/usr/bin/env python3
import math
ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())
dx, dy = map(int, input().split())

ab = (bx - ax, by - ay)
ad = (dx - ax, dy - ay)
a = (ad[0] * ab[1] - ad[1] * ab[0]) < 0

ba = (ax - bx, ay - by)
bc = (cx - bx, cy - by)
b = (ba[0] * bc[1] - ba[1] * bc[0]) < 0

cb = (bx - cx, by - cy)
cd = (dx - cx, dy - cy)
c = (cb[0] * cd[1] - cb[1] * cd[0]) < 0

dc = (cx - dx, cy - dy)
da = (ax - dx, ay - dy)
d = (dc[0] * da[1] - dc[1] * da[0]) < 0

if a and b and c and d:
  print('Yes')
else:
  print('No')