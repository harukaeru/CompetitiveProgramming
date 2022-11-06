#!/usr/bin/env python3.8
A = tuple(map(int, input().split()))  # a
B = tuple(map(int, input().split()))  # b
C = tuple(map(int, input().split()))  # c
D = tuple(map(int, input().split()))  # d

def cross(t, u):
  return t[0] * u[1] - t[1] * u[0]

ab = (B[0] - A[0], B[1] - A[1])
ac = (C[0] - A[0], C[1] - A[1])
ad = (D[0] - A[0], D[1] - A[1])

cd = (D[0] - C[0], D[1] - C[1])
cb = (B[0] - C[0], B[1] - C[1])
ca = (A[0] - C[0], A[1] - C[1])

if cross(ab, ac) == 0 and cross(ab, ad) == 0 and cross(cd, cb) == 0 and cross(cd, ca) == 0:
  if B > A:
    A, B = B, A
  if D > C:
    C, D = D, C
  if max(B, D) <= min(A, C):
    print('Yes')
  else:
    print('No')
  exit()

is_sep_ab = ((cross(ab, ac) >= 0) == (cross(ab, ad) <= 0)) or ((cross(ab, ac) <= 0) == (cross(ab, ad) >= 0))
is_sep_cd = ((cross(cd, cb) >= 0) == (cross(cd, ca) <= 0)) or ((cross(cd, cb) <= 0) == (cross(cd, ca) >= 0))
if is_sep_ab and is_sep_cd:
  print('Yes')
else:
  print('No')