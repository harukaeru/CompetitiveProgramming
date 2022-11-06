#!/usr/bin/env python3.8
A,B,C = map(int, input().split())
if A <= C <= B:
  print('Yes')
else:
  print('No')