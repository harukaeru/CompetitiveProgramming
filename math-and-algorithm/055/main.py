#!/usr/bin/env python3.8
MOD = 10 ** 9 + 7
class Matrix:
  def __init__(self, matrix):
    self.matrix = matrix
  
  def __mul__(self, other):
    res = []
    for i in range(len(self.matrix)):
      cres = []
      for k in range(len(other.matrix)):
        t = 0
        for j in range(len(self.matrix[i])):
          t += self.matrix[i][j] * other.matrix[j][k]
        cres.append(t % MOD)
      res.append(cres)
    return Matrix(res)


m = Matrix([
  [0, 1],
  [1, 2],
])

def doub(n):
  y = m
  ans = Matrix([
    [1, 0],
    [0, 1],
  ])
  for i in range(60):
    if (n & (1 << i)) != 0:
      ans *= y
    y *= y
  return ans

N = int(input())
# for r in doub(1).matrix:
#   print(r)
# for i in range(10):
#   print(sum(doub(i).matrix[1]))
# print(sum(doub(N - 3).matrix[1]) % MOD)
print(sum(doub(N - 2).matrix[1]) % MOD)
# print(sum(doub(N - 1).matrix[1]) % MOD)
# print(sum(doub(N - 0).matrix[1]) % MOD)