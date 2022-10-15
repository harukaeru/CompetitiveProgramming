#!/usr/bin/env pypy3
from collections import defaultdict
import bisect
H, W, rs, cs = map(int, input().split())
N = int(input())

h_defa = [-1, W]
w_defa = [-1, H]
h_walls = defaultdict(list)
w_walls = defaultdict(list)
for i in range(N):
  r, c = map(int, input().split())
  h_walls[r].append(c)
  w_walls[c].append(r)

for h in h_walls.values():
  h.sort()
for w in w_walls.values():
  w.sort()

# for h in h_walls:
#   print(h)
# print('--------')
# for w in w_walls:
#   print(w)
# print('--------')
  
Q = int(input())
commands = []
for i in range(Q):
  d, l = input().split()
  commands.append((d, int(l)))

commands.reverse()
  
q = []
q.append((rs, cs))

while len(q) > 0:
  i, j = q.pop()
  if len(commands) == 0:
    exit()
  # print('(i,j) => ', i, j)
  cmd = commands.pop()
  nex = None
  l = cmd[1]
  if cmd[0] == 'U':
    ww = w_walls[j]
    upos = bisect.bisect_right(ww, i) - 1
    if upos == -1:
      t = 1
    else:
      t = ww[upos] + 1

    nex = (max(i - l, t), j)
  elif cmd[0] == 'D':
    ww = w_walls[j]
    dpos = bisect.bisect_right(ww, i)
    if dpos == len(ww):
      t = H
    else:
      t = ww[dpos] - 1
    nex = (min(i + l, t), j)
  elif cmd[0] == 'L':
    hh = h_walls[i]
    lpos = bisect.bisect_right(hh, j) - 1
    if lpos == -1:
      t = 1
    else:
      t = hh[lpos] + 1
    nex = (i, max(j - l, t))
  elif cmd[0] == 'R':
    hh = h_walls[i]
    rpos = bisect.bisect_right(hh, j)
    if rpos == len(hh):
      t = W
    else:
      t = hh[rpos] - 1
    nex = (i, min(j + l, t))
  print(*nex)
  q.append(nex)