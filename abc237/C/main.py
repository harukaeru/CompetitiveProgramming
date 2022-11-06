#!/usr/bin/env python3.8
s = input()


left_a_count = 0
for x in s:
  if x == 'a':
    left_a_count += 1
  else:
    break

t = s[::-1]
right_a_count = 0
for x in t:
  if x == 'a':
    right_a_count += 1
  else:
    break

mid = s[left_a_count:len(s) - right_a_count]

if mid == mid[::-1] and left_a_count <= right_a_count:
  print('Yes')
else:
  print('No')