#!/usr/bin/env python3.8
T = int(input())

for i in range(T):
  case = list(map(int, input().split()))
  x1, y1, r1 = case[0], case[1], case[2]
  x2, y2, r2 = case[3], case[4], case[5]

  dd = ((x2 - x1) ** 2) + ((y2 - y1) ** 2)
  rr = (r1 + r2) ** 2

  rr2 = (max(r1, r2) - min(r1, r2)) ** 2
  
  print('Yes' if rr2 <= dd and dd <= rr else 'No')