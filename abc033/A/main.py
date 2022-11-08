#!/usr/bin/env python3.8
N = input()

if len(set(N)) == 1:
  print('SAME')
else:
  print('DIFFERENT')