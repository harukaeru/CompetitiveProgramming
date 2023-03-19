#!/usr/bin/env pypy3
L,N1,N2=map(int, input().split())
UP = []
for i in range(N1):
  v, l = map(int, input().split())
  UP.append([v, l])

DOWN = []
for i in range(N2):
  v, l = map(int, input().split())
  DOWN.append([v, l])

cur_up = None
cur_down = None

l = 0
r = 0
cnt = 0
while l < N1 or r < N2:
  if cur_up is None:
    cur_up = UP[l]
    l += 1
  if cur_down is None:
    cur_down = DOWN[r]
    r += 1

  if cur_up[0] == cur_down[0]:
    if cur_up[1] > cur_down[1]:
      cnt += cur_down[1]
      cur_up = [cur_up[0], cur_up[1] - cur_down[1]]
      cur_down = None
    elif cur_up[1] < cur_down[1]:
      cnt += cur_up[1]
      cur_down = [cur_down[0], cur_down[1] - cur_up[1]]
      cur_up = None
    else:
      cnt += cur_up[1]
      cur_up = None
      cur_down = None
  else:
    if cur_up[1] > cur_down[1]:
      cur_up = [cur_up[0], cur_up[1] - cur_down[1]]
      cur_down = None
    elif cur_up[1] < cur_down[1]:
      cur_down = [cur_down[0], cur_down[1] - cur_up[1]]
      cur_up = None
    else:
      cur_up = None
      cur_down = None

print(cnt) 
  