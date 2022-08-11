#!/usr/bin/env python3
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

if max(A) > min(B):
  print(0)
  exit()

print(min(B) - max(A) + 1)