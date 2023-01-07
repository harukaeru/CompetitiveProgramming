#!/usr/bin/env python3.8
N = int(input())

def down(a):
  d = len(str(a))
  if d == 1:
    return
  
  return 10 ** (d - 1) - 1

def calc(x, y):
  print(x, y)
  # x,y = min(x, y), max(x, y)

  xd = len(str(x))
  yd = len(str(y))

  if xd == 1 and yd == 1:
    return min(x, y)

  if xd == 1:
    c = ord(str(y)[0]) - ord('0')
    d = ord(str(y)[-1]) - ord('0')
    if c > d:
      c -= 1

    mid_d = yd - 2
    cnt = 10 ** mid_d
    tot = c * cnt
    tot += calc(x, down(y))
    return tot
  
  if yd == 1:
    c = ord(str(x)[0]) - ord('0')
    d = ord(str(x)[-1]) - ord('0')
    if c > d:
      c -= 1

    mid_d = xd - 2
    cnt = 10 ** mid_d
    tot = c * cnt
    return tot

  a = ord(str(x)[0]) - ord('0')
  b = ord(str(x)[-1]) - ord('0')
  if b == 0:
    return calc(x - 1, y)

  c = ord(str(y)[0]) - ord('0')
  d = ord(str(y)[-1]) - ord('0')
  if d == 0:
    return calc(x, y - 1)

  if a < b:
    b = a

  mid_xd = xd - 2
  xcnt = 10 ** mid_xd
  mid_yd = yd - 2
  ycnt = 10 ** mid_yd

  c = a - 1 if a >= b else a
  tot = (a * b - c) * xcnt * ycnt
  print(a * b)
  print('  a,b,tot', tot)

  downed_x = down(x)
  downed_y = down(y)
  if downed_x:
    tot += calc(downed_x, y)
  if downed_y:
    tot += calc(x, downed_y)

  return tot
  

print(calc(N, N))