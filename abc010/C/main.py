#!/usr/bin/env python3.8
import math

txa,tya,txb,tyb,T,V = map(int, input().split())
n = int(input())

def calc(a, b):
  d2 = (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
  return math.sqrt(d2)

capacity = T * V

for i in range(n):
  px, py = map(int, input().split())
  half1 = calc((txa, tya), (px, py))
  half2 = calc((px, py), (txb, tyb))

  tot = half1 + half2
  if (tot) <= capacity:
    print('YES')
    exit()
print('NO')