#!/usr/bin/env python3
N = int(input())
A = []
for i in range(N):
  A.append(int(input()))

m_a = max(A)
if A.count(m_a) >= 2:
  for i in range(N):
    print(m_a)
  exit()

m_a_idx = A.index(m_a)
A.remove(m_a)

second_m_a = max(A)
for i in range(N):
  if i == m_a_idx:
    print(second_m_a)
  else:
    print(m_a)