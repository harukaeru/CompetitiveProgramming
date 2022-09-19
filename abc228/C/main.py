#!/usr/bin/env python3
import bisect
N, K = map(int, input().split())
scores = []
for i in range(N):
  P = list(map(int, input().split()))
  scores.append(sum(P))

thirds = list(sorted(scores))
for s in scores:
  fourth = s + 300
  low_rank = bisect.bisect_right(thirds, fourth)
  rank = len(scores) + 1 - low_rank
  if rank <= K:
    print('Yes')
  else:
    print('No')
  # print(rank)