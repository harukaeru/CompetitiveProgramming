#!/usr/bin/env python3.8
X,Y,A,B = map(int, input().split())

cnt = 0
while X * A <= B:
  X *= A
  if X >= Y:
    print(cnt)
    exit()
  cnt += 1

c = (Y - X) // B
if X + c * B >= Y:
  c -= 1

print(cnt + c)