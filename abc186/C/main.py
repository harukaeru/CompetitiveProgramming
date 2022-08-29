#!/usr/bin/env python3
N = int(input())

def to_8bit(v):
  result = ''
  while v != 0:
    result = str(v % 8) + result
    v //= 8
  return result

cnt = 0
for i in range(1, N + 1):
  if '7' not in str(i) and '7' not in to_8bit(i):
    cnt += 1

print(cnt)
