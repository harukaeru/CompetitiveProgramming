#!/usr/bin/env python3
A = set([1,3,5,7,8,10,12])
B = set([4,6,9,11])
C = set([2])

x, y = map(int, input().split())
if x in A and y in A:
  print('Yes')
  exit()
if x in B and y in B:
  print('Yes')
  exit()
if x in C and y in C:
  print('Yes')
  exit()

print('No')