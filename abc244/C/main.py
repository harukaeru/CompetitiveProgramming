#!/usr/bin/env python3.8
N = int(input())
k = set([i + 1 for i in range(2 * N + 1)])

def remove(k, i):
  k.remove(i)

remove(k, 1)
print(1)
while True:
  a = int(input())
  if a == 0:
    break

  remove(k, a)
  p = k.pop()
  print(p)