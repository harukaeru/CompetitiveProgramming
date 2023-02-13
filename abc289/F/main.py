#!/usr/bin/env pypy3
sx,sy=map(int, input().split())
gx,gy=map(int, input().split())
a,b,c,d=map(int, input().split())

anses = []

def flip(p, q):
  anses.append((p, q))
  global sx
  global sy
  sx = 2 * p - sx
  sy = 2 * q - sy
  # print('sx,sy', sx, sy)

if a == b and sx != gx:
  flip(a, c)
if c == d and sy != gy:
  flip(a, c)

if a != b:
  while (sx < gx):
    flip(a, c)
    flip(a + 1, c)
  while sx > gx:
    flip(a + 1, c)
    flip(a, c)

if c != d:
  while (sy < gy):
    flip(a, c)
    flip(a, c + 1)
  while sy > gy:
    flip(a, c + 1)
    flip(a, c)

if (sx == gx and sy == gy):
  print('Yes')
  for an in anses:
    print(*an)
else:
  print('No')