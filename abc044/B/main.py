#!/usr/bin/env python3.8
from collections import Counter
w = input()

if all(v % 2 == 0 for v in Counter(w).values()):
  print('Yes')
else:
  print('No')