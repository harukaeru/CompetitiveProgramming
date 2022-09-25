#!/usr/bin/env python3
n, r = map(int, input().split())


def factorial(a):
  ans = 1
  for i in range(1, a + 1):
    ans *= i
  return ans

print(factorial(n) // factorial(r) // factorial(n - r))