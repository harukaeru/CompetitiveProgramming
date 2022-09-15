#!/usr/bin/env python3
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

if r1 == r2 and c1 == c2:
  print(0)
  exit()

x1 = r1 + c1
y1 = r1 - c1
x2 = r2 + c2
y2 = r2 - c2

if x1 == x2 or y1 == y2 or abs(r1 - r2) + abs(c1 - c2) <=3:
  print(1)
  exit()

if abs(x1 - x2) <= 3 or abs(y1 - y2) <= 3:
  print(2)
elif x1 % 2 == x2 % 2:
  print(2)
elif abs(r1 - r2) + abs(c1 - c2) <= 6:
  print(2)
else:
  print(3)
