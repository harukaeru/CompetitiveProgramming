#!/usr/bin/env python3.8
import string


S = input()

import re
r = re.compile('^[A-Z]\d{6}[A-Z]$')
s = r.search(S)
if s:
  if S[1:-1].startswith('0'):
    print('No')
    exit()
  print('Yes')
else:
  print('No')