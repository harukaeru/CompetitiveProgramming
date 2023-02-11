#!/usr/bin/env python3.8
sx,sy=map(int, input().split())
tx,ty=map(int, input().split())
a,b,c,d=map(int, input().split())

P = 30

nx_range = [sx, sx]
for i in range(P):
  dxl1 = a - nx_range[0]
  dxl2 = b - nx_range[0]

  dxr1 = a - nx_range[1]
  dxr2 = b - nx_range[1]

  aa = min(nx_range[0] + dxl1 * 2, nx_range[0] + dxl2 * 2)
  aa2 = min(nx_range[1] + dxr1 * 2, nx_range[1] + dxr2 * 2)
  xl = min(aa, aa2)

  bb = max(nx_range[0] + dxl1 * 2, nx_range[0] + dxl2 * 2)
  bb2 = max(nx_range[1] + dxr1 * 2, nx_range[1] + dxr2 * 2)
  xr = max(bb, bb2)

  nx_range = [xl, xr]
  print(nx_range)
  if xl <= tx <= xr:
    print('Yes')
    exit()

print('No')