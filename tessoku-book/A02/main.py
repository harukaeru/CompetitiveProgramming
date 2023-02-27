#!/usr/bin/env python3.8
N,X=map(int, input().split())
A = list(map(int, input().split()))
if X in A:
  print('Yes')
else:
  print('No')