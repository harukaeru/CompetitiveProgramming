#!/usr/bin/env python3.8
from collections import Counter
n = int(input())
a = list(map(int, input().split()))

b = []
c = []

for i, x in enumerate(a):
  if i % 2 == 0:
    b.append(x)
  else:
    c.append(x)

def sort_by_index1(b):
  return -b[1]

b_counter = list(sorted(Counter(b).items(), key=sort_by_index1))
c_counter = list(sorted(Counter(c).items(), key=sort_by_index1))

rest_b_counter = [(b[0], n // 2 - b[1]) for b in b_counter] + [(-1, n // 2)]
rest_c_counter = [(c[0], n // 2 - c[1]) for c in c_counter] + [(-1, n // 2)]

minimum_group = set([rest_c_counter[0][0]])
minimum_rest = rest_c_counter[0][1]
second_minimum_rest = None
for rest_c in rest_c_counter[1:]:
  if rest_c[1] == minimum_rest:
    minimum_group.add(rest_c[0])
  else:
    second_minimum_rest = rest_c[1]
    break

total = 999999999999999999
for bx in rest_b_counter:
  b_value = bx[0]
  b_count = bx[1]
  c_count = second_minimum_rest if b_value in minimum_group and len(minimum_group) == 1 else minimum_rest
  # print(b_value, '->', b_count, c_count)
  total = min(total, b_count + c_count)

print(total)