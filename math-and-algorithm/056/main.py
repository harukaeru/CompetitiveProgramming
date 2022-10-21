#!/usr/bin/env python3
N = int(input())
MOD = 10 ** 9 + 7

class Matrix:
  def __init__(self, matrix):
    self.matrix = matrix
  
  def __mul__(self, other):
    result = []
    for i in range(len(self.matrix)):
      vals = []
      for k in range(len(other.matrix[0])):
        t = 0
        for j in range(len(self.matrix[i])):
          t += self.matrix[i][j] * other.matrix[j][k]
        #   print('i,j,k', i, j, k, '=>', self.matrix[i][j] + other.matrix[j][k])
        # print(t)
        vals.append(t % MOD)
      result.append(vals)
    return Matrix(result)

e = Matrix([
  [1, 0, 0],
  [0, 1, 0],
  [0, 0, 1],
])

m = Matrix([
  [0, 1, 0],
  [0, 0, 1],
  [1, 1, 1],
])

def doub(n):
  y = m
  ans = e
  for i in range(60):
    if (n & (1 << i)) != 0:
      ans *= y
    y *= y
  return ans

# def show(matrix):
#   for m in matrix.matrix:
#     print(m)
#   print('------')
# 
# show(e * e)
# print(show(doub(N - 3)))
# mat = doub(N - 3).matrix
mat = doub(N -3) * Matrix([
  [1],
  [1],
  [2],
])

print(mat.matrix[-1][0] % MOD)