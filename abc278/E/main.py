#!/usr/bin/env pypy3
H, W, N, h, w = map(int, input().split())
 
q = set()
HW = []
for i in range(H):
  l = list(map(int, input().split()))
  s = set(l)
  q.update(s)
  HW.append(l)

q = list(q)

INF = 99999999
min_is = [INF] * len(q)
min_js = [INF] * len(q)
max_is = [-1] * len(q)
max_js = [-1] * len(q)

for xi, x in enumerate(q):
  for i in range(H):
    for j in range(W):
      if HW[i][j] == x:
        min_is[xi] = min(min_is[xi], i)
        min_js[xi] = min(min_js[xi], j)
        max_is[xi] = max(max_is[xi], i)
        max_js[xi] = max(max_js[xi], j)

# for xi, x in enumerate(q):
#   print(x, (min_is[xi], min_js[xi]), '~',  (max_is[xi], max_js[xi]))
# print('--------')


for i in range(H - h + 1):
  a = []
  for j in range(W - w + 1):
    cnt = 0
    ie = i + h - 1
    je = j + w - 1
    for xi, x in enumerate(q):
      if (min_is[xi] < i) or (ie < max_is[xi]) or (min_js[xi] < j or je < max_js[xi]):
        # print('x' ,x)
        cnt += 1
    a.append(cnt)
  print(*a)