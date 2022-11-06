#!/usr/bin/env python3.8
MOD = 998244353
N = int(input())

d = len(str(N))
cnt = 0
for i in range(d):
  k = i + 1
  base = 10 ** (k - 1)
  if i == d - 1:
    m = N
  else:
    m = 10 ** k - 1

  base_cnt = 1
  m_cnt = m - base + 1

  c = (m_cnt - base_cnt + 1) * (base_cnt + m_cnt) // 2
  cnt += c % MOD

print(cnt % MOD)