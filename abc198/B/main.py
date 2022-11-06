#!/usr/bin/env python3.8
N = input()

for i in range(10):
  s = '0' * i + N
  if s == s[::-1]:
    print("Yes")
    exit()
print("No")