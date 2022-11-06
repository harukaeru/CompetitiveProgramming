#!/usr/bin/env python3.8
import math
N = int(input())
A = list(map(int, input().split()))

g = 0
for a in A:
  g = math.gcd(g, a)

C2 = []
C3 = []

s = 0
for a in A:
  a //= g
  c2 = 0
  c3 = 0
  while a % 2 == 0:
    a //= 2
    c2 += 1
  while a % 3 == 0:
    a //= 3
    c3 += 1
  
  if a != 1:
    print(-1)
    exit()

  s += c2 + c3

print(s)