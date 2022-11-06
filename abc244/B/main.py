#!/usr/bin/env python3.8
import operator
N = int(input())
S = input()

directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
current_direction_idx = 0

pos = (0, 0)
for s in S:
  if s == 'S':
    direction = directions[current_direction_idx]
    pos = tuple(map(operator.add, pos, direction))
  else:
    current_direction_idx = (current_direction_idx + 1) % 4
print(*pos)