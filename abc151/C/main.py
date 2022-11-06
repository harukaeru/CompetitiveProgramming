#!/usr/bin/env python3.8
N, M = map(int, input().split())

ac_flags = {}
wa_counter = {}
ac_count = 0
for i in range(M):
  p, S = input().split()
  p = int(p)

  # 1度以上正解しているならあとの操作は無視
  if ac_flags.get(p):
    continue

  # 以下は「1度も正解していない」とき
  if S == 'AC':
    ac_count += 1
    ac_flags[p] = True
    continue
      
  # WA
  wa_counter.setdefault(p, 0)
  wa_counter[p] += 1

wa_count = 0
for k in ac_flags:
  wa_count += wa_counter.get(k, 0)

print(ac_count, wa_count)