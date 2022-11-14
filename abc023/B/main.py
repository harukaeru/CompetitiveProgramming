#!/usr/bin/env python3.8
N = int(input())
S = input()

cache = {}
def f(n):
  if n == 0:
    return 'b'
  if cache.get(n):
    return cache[n]
  if n % 3 == 1:
    cache[n] = 'a' + f(n - 1) + 'c'
  elif n % 3 == 2:
    cache[n] = 'c' + f(n - 1) + 'a'
  else:
    cache[n] = 'b' + f(n - 1) + 'b'
  return cache[n]

if S == 'b':
  print(0)
  exit()

for i in range(1, 101):
  if f(i) == S:
    print(i)
    exit()
print(-1)