#!/usr/bin/env python3.8
S = input()
if len(set(S)) == len(S):
  print('yes')
else:
  print('no')