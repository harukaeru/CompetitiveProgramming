#!/usr/bin/env python3
import heapq
Q = int(input())

s_counter = {}
min_h = []
max_h = []
erased_cache = set()

for i in range(Q):
  query = list(map(int, input().split()))
  # print('query---', query)
  if query[0] == 1:
    x = query[1]
    s_counter.setdefault(x, 0)
    s_counter[x] += 1
    heapq.heappush(min_h, x)
    heapq.heappush(max_h, -x)
    if x in erased_cache:
      erased_cache.remove(x)
    # print('min_h', min_h)
    # print('min_h', max_h)
  elif query[0] == 2:
    x, c = query[1:]
    if s_counter.get(x) is None:
      continue
    v = min(c, s_counter[x])
    s_counter[x] -= v
    if s_counter[x] == 0:
      erased_cache.add(x)
  elif query[0] == 3:
    # print('min_h', min_h)
    # print('max_h', max_h)
    # print('erased', erased_cache)
    while 1:
      mi = heapq.heappop(min_h)
      if mi in erased_cache:
        continue
      else:
        heapq.heappush(min_h, mi)
        break
    while 1:
      ma = -heapq.heappop(max_h)
      if ma in erased_cache:
        continue
      else:
        heapq.heappush(max_h, -ma)
        break
    print(ma - mi)
