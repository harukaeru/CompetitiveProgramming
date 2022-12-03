#!/usr/bin/env python3.8
H, W = map(int, input().split())
c = 0
for i in range(H):
  s = input()
  c += s.count('#')
print(c)