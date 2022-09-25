#!/usr/bin/env python3
A, B = map(int, input().split())

def gcd(a, b):
  if b == 0:
    return a
  if b > a:
    return gcd(b, a)
  c = a % b
  return gcd(b, c)

print(gcd(A, B))