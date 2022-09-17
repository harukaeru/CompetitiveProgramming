#!/usr/bin/env python3
S = []

j_array = []
i_array = []
for i in range(10):
  s = input()
  if '#' in s:
    i_array.append(i)
    j_array.append(s.index('#'))
    count = s.count('#')

print(min(i_array) + 1, max(i_array) + 1)
print(min(j_array) + 1, max(j_array) + count)