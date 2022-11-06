#!/usr/bin/env python3.8
X = int(input())

while 1:
  is_prime = True
  for i in range(2, X):
    if X % i == 0:
      is_prime = False
      break

  if is_prime:
    print(X)
    exit()
  X += 1