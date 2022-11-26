#!/usr/bin/env python3.8
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import inv
import numpy as np
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = [0] * N
B[0] = 1
B = np.array(B)

matrixes = []
invs = []
for i in range(M):
  a = A[i]
  b = a - 1
  x = lil_matrix((N, N))
  for j in range(N):
    if j == a:
      x[j,b] = 1
    elif j == b:
      x[j,a] = 1
    else:
      x[j,j] = 1
  matrixes.append(x)
  invs.append(inv(x))

invs.reverse()
print('matrixes')
for ma in matrixes:
  print(ma.todense())

cinvs = [None] * (len(invs))
cinvs[0] = invs[0]
for i in range(1, len(invs)):
  cinvs[i] = invs[i].multiply(cinvs[i - 1])

cmatrixes = [None] * (len(matrixes))
cmatrixes[0] = matrixes[0]
for i in range(1, len(matrixes)):
  cmatrixes[i] = matrixes[i].multiply(cmatrixes[i - 1])


print('B', B)
for cc in cmatrixes:
  print(cc.todense())

C = cmatrixes[-1].multiply(B)

print('C', C)
print('?')
for ma in matrixes:
  print(ma.todense())
  print('-----------')

print('-----------------LL-')
for i in range(M):
  if i == 0:
    x = cinvs[0].multiply(C)
    print(x.todense())
  else:
    x = cmatrixes[i - 1].multiply(cinvs[i]).multiply(C)
    print(x.todense())
# print(matrixes)

# ナイーブ解
# for i in range(M):
#   for j in range(M):
#     if i == j:
#       continue
#     a = A[j]
#     a -= 1
#     B[a], B[a + 1] = B[a + 1], B[a]
#   print(B.index(1) + 1)