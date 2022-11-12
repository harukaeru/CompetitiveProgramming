#!/usr/bin/env python3.8
sa = list(input())
sb = list(input())
sc = list(input())
sa.reverse()
sb.reverse()
sc.reverse()

nex = 'a'
cur = sa
while len(sa) != 0 or len(sb) != 0 or len(sc) != 0:
  nex = cur.pop()
  if nex == 'a':
    cur = sa
  elif nex == 'b':
    cur = sb
  else:
    cur = sc
  if len(cur) == 0:
    print(nex.upper())
    exit()