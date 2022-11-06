#!/usr/bin/env python3.8
X, Y, Z = map(int, input().split())


if X < 0:
  X = -X
  Y = -Y
  Z = -Z

if X < Y:
  print(X)
elif Y < 0:
  print(X)
else:
  if Y < Z:
    print(-1)
  elif 0 < Z:
    print(X)
  else:
    print((-Z) * 2 + X)