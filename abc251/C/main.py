#!/usr/bin/env python3
N = int(input())

submitted = set()
top_original = None
top_score = 0
for i in range(N):
  s, t = input().split()
  t = int(t)
  if s in submitted:
    continue

  if t > top_score:
    top_original = i
    top_score = t

  submitted.add(s)

print(top_original + 1)