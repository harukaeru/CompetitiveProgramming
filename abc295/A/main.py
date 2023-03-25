#!/usr/bin/env python3.8
N = int(input())
W = input().split()

words = set([
  'and',
  'not',
  'that',
  'the',
  'you'
])

for w in W:
  if w in words:
    print('Yes')
    exit()
print('No')