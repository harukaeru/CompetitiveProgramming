#!/usr/bin/env python3
N = int(input())
def get_i_query(s, e):
  print('?', s, e, 1, N)
  ans = int(input())
  if ans == -1:
    raise ValueError
  return ans == e - s + 1
  
def get_j_query(s, e):
  print('?', 1, N, s, e)
  ans = int(input())
  if ans == -1:
    raise ValueError
  return ans == e - s + 1

i_start = 1
i_end = N
j_start = 1
j_end = N

while i_end - i_start > 1:
  i_mid = (i_start + i_end) // 2
  same = get_i_query(i_start, i_mid)
  if same:
    i_start = i_mid + 1
  else:
    i_end = i_mid

same = get_i_query(i_start, i_start)
i_ans = i_end if same else i_start

while j_end - j_start > 1:
  j_mid = (j_start + j_end) // 2
  same = get_j_query(j_start, j_mid)
  if same:
    j_start = j_mid + 1
  else:
    j_end = j_mid

same = get_j_query(j_start, j_start)
j_ans = j_end if same else j_start

print('!', i_ans, j_ans)