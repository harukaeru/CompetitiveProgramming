#!/usr/bin/env python3.8
H,W=map(int, input().split())

if H % 3 == 0 or W % 3 == 0:
  print(0)
  exit()


ans = H * W

for i in range(2):
  for w1 in range(1, W):
    a = w1 * H
    b = H // 2 * (W - w1)
    c = H * (W - w1) - b
    ans = min(ans, max(a,b,c) - min(a,b,c))

    b = H * ((W - w1) // 2)
    c = H * (W - w1) - b
    ans = min(ans, max(a,b,c) - min(a,b,c))
  H,W=W,H
print(ans)

