#!/usr/bin/env python3.8
a,b,c= map(int, input().split())
if a + b == c and a - b == c:
  print('?')
elif a + b == c:
  print('+')
elif a - b == c:
  print('-')
else:
  print('!')