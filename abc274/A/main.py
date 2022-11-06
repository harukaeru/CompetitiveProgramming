#!/usr/bin/env python3.8
A, B = map(int, input().split())

P = B * 1000 // A
S = (B * 10000 // A) % 10
if S >= 5:
  P += 1
print('{:.3f}'.format(P / 1000))