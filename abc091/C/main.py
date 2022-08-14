#!/usr/bin/env python3
N = int(input())

reds = []
for i in range(N):
  red = tuple(map(int, input().split()))
  reds.append(red)

blues = []
for i in range(N):
  blue = tuple(map(int, input().split()))
  blues.append(blue)

blues.sort()

cnt = 0
# from pprint import pprint
# print('----reds')
# pprint(reds)
# print('----blues')
# pprint(blues)
for blue in blues:
  red_to_remove = None
  max_v = -1
  for red in reds:
    if blue[0] >= red[0] and blue[1] >= red[1]:
      if max_v < red[1]:
        max_v = red[1]
        red_to_remove = red
  if red_to_remove is not None:
    reds.remove(red_to_remove)
    cnt += 1

print(cnt)