#!/usr/bin/env python3
X, A, D, N = map(int, input().split())

if D >= 0:
  max_s = A + (N - 1) * D
  min_s = A
else:
  min_s = A + (N - 1) * D
  max_s = A

if min_s <= X <= max_s:
  if D != 0:
    rest = (X - min_s) % D 
  else:
    rest = X - A
  d = min(abs(abs(D) - abs(rest)), abs(rest))
  print(d)
  exit()

print(min([abs(X - min_s), abs(X - max_s)]))