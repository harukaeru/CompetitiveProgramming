#!/usr/bin/env python3.8
N = int(input())
A = list(map(int, input().split()))

def gcd(a, b):
  if b == 0:
    return a
  
  if b > a:
    return gcd(b, a)
  return gcd(b, a % b)

current = 0
for a in A:
  current = gcd(a, current)
print(current)