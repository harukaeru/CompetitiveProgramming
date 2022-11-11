#!/usr/bin/env python3.8
A, B, C = map(int, input().split())

for i in range(1, 101):
  if A * i % B == C:
    print('YES')
    exit()
print('NO')