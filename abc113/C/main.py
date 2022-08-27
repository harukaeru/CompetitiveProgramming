#!/usr/bin/env python3
n, m = map(int, input().split())

ps = {}

lst = []
for i in range(m):
  p_i, y_i = map(int, input().split())
  ps.setdefault(p_i, []).append(y_i)
  lst.append((p_i, y_i))

for key, values in ps.items():
  values.sort()
  values = [(value, seq + 1) for seq, value in enumerate(values)]
  ps[key] = dict(values)
  # print(key, '->', values)

for i in range(m):
  p_i, y_i = lst[i]
  seq = ps[p_i][y_i]
  print(f'{p_i:06d}{seq:06d}')