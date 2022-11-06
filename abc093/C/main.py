#!/usr/bin/env python3.8
a, b, c = map(int, input().split())

m = max([a, b, c])

x = m - a
y = m - b
z = m - c
if (x + y + z) % 2 == 0:
  print((x + y + z) // 2)
  exit()

ans = []
for p in [a, b, c]:
  if p == m:
    ans.append(0)
  else:
    ans.append(m + 1 - p)

print(sum(ans) // 2 + 1)