#!/usr/bin/env python3.8
from collections import Counter

def f(text):
  return tuple(sorted(Counter(text).values()))

s, t = input(), input()

if f(s) == f(t):
  print('Yes')
else:
  print('No')