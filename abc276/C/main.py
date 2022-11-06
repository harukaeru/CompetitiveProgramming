#!/usr/bin/env python3.8
import sys
print('sy', sys.version)
n = int(input())
p = list(map(int, input().split()))
 
j = n - 2
while p[j] < p[j + 1]:
  j -= 1

k = n - 1
while p[j] < p[k]:
  k -= 1

p[j], p[k] = p[k], p[j]
print(*p[:j + 1], *p[:j:-1])
print('p', p)