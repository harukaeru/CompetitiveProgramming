#!/usr/bin/env python3
N = int(input())
A = list(map(int, input().split()))

def gcd(a, b):
  if b == 0:
    return a

  if b > a:
    return gcd(b, a)

  return gcd(b, a % b)

def lcm(a, b):
  return a * b // gcd(a, b)

current = A[0]
for a in A[1:]:
  current = lcm(a, current)
  
print(current)