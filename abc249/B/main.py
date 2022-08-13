#!/usr/bin/env python3
S = input()

is_splendid = any(s.islower() for s in S) and any(s.isupper() for s in S) and len(set(S)) == len(S)
if is_splendid:
  print('Yes')
else:
  print('No')