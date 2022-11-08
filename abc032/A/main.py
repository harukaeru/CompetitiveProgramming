#!/usr/bin/env python3.8
a = int(input())
b = int(input())
n = int(input())

for i in range(n, 20001 + a * b):
  if (i % a == 0) and (i % b == 0):
    print(i)
    exit()