#!/usr/bin/env python3.8
from collections import Counter
a = map(int, input().split())

counter = Counter(a)

is_fullhouse = 2 in counter.values() and 3 in counter.values()
  
if is_fullhouse:
  print('Yes')
else:
  print('No')