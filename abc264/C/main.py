#!/usr/bin/env pypy3
H1, W1 = map(int, input().split())
A = []
for i in range(H1):
  a = list(map(int, input().split()))
  A.append(a)

H2, W2 = map(int, input().split())
B = []
for i in range(H2):
  b = list(map(int, input().split()))
  B.append(b)

from pprint import pprint
# pprint(A)
# print('-----')
# pprint(B)

for i in range(2 ** H1):
  p = i
  hs = []
  for h in range(H1):
    if p % 2:
      hs.append(h)
    p //= 2
  for j in range(2 ** W1):
    if i == 0 and j == 0:
      continue

    q = j
    ws = []
    for w in range(W1):
      if q % 2:
        ws.append(w)
      q //= 2

    if len(hs) != len(B) or len(ws) != len(B[0]):
      continue

    is_matched = True
    for bi in range(len(B)):
      for bj in range(len(B[bi])):
        hi = hs[bi]
        wj = ws[bj]
        try:
          is_matched &= B[bi][bj] == A[hi][wj]
        except:
          is_matched = False
    if is_matched:
      print('Yes')
      exit()
print('No')
