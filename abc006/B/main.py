#!/usr/bin/env python3.8
a,b,c = 0, 0, 1

n = int(input())
for i in range(n - 1):
  a,b,c = b,c, (a + b + c) 

print(a)