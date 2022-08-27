#!/usr/bin/env python3
s1, s2, s3 = input().split()
t1, t2, t3 = input().split()

if ((s1 != t1) + (s2 != t2) + (s3 != t3)) != 2:
  print('Yes')
else:
  print('No')