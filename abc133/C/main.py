#!/usr/bin/env python3.8
L, R = map(int, input().split())


m = 999999999
i_cnt = 0
for i in range(L, R):
  i_cnt += 1
  if i_cnt > 2019:
    break

  j_cnt = 0
  for j in range(L + 1, R + 1):
    j_cnt += 1
    v = (i % 2019) * (j % 2019) % 2019
    m = min(m, v)
    # print('j', j, j % 2019)
    if j_cnt > 2019:
      break

print(m)