#!/usr/bin/env python3.8
A, B = map(int, input().split())

score = 0
for i in range(3):
  a = A & (1 << i)
  b = B & (1 << i)
  if a or b:
    score += 1 << i
print(score)