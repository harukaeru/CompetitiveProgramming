#!/usr/bin/env python3
N = int(input())
P = list(map(int, input().split()))

for i in range(N - 2, -1, -1):
  A = P[i:N]
  B = list(sorted(P[i:N]))
  if A == B:
    continue

  # if len(A) == 2:
  #   print(*(P[0:i] + B))
  #   exit()
  # print('A', A)
  # print('B', B)
  escaped_smallest = False
  decided = False
  sm = 1
  for p in range(len(A) - 1):
    if not escaped_smallest and A[p] == sm:
      sm += 1
      continue
    escaped_smallest = True

    if not decided:
      k = 1
      while not decided:
        m = A[p] - k
        try:
          mi = A.index(m)
          decided = True
        except:
          pass
        k += 1
    else:
      m = max(A[p:])
      mi = A.index(m)
    A[p], A[mi] = A[mi], A[p]
  print(*(P[0:i] + A))
  exit()