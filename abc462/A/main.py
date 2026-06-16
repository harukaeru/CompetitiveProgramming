#!/usr/bin/env python3.8
s = input()
for ss in s:
  try:
    ss = int(ss)
  except:
    continue
  print(ss, end='')
print()