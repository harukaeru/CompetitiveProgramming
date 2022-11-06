#!/usr/bin/env python3.8
N = int(input())

MOD = 10 ** 9
A = [
  [1, 1],
  [1, 0],
]

class Matrix:
  def __init__(self, matrix):
    self.matrix = matrix
  
  def __mul__(self, other):
    return Matrix([
      [
        (self.matrix[0][0] * other.matrix[0][0] + self.matrix[0][1] * other.matrix[1][0]) % MOD,
        (self.matrix[0][0] * other.matrix[0][1] + self.matrix[0][1] * other.matrix[1][1]) % MOD
      ],
      [
        (self.matrix[1][0] * other.matrix[0][0] + self.matrix[1][1] * other.matrix[1][0]) % MOD,
        (self.matrix[1][0] * other.matrix[0][1] + self.matrix[1][1] * other.matrix[1][1]) % MOD
      ],
    ])

def fib(n):
  y = Matrix(A)
  ans = Matrix([
    [1, 0],
    [0, 1],
  ])
  for i in range(60):
    if (n & (1 << i)) != 0:
      ans *= y
    y *= y
  return ans

print(sum(fib(N - 1).matrix[1]) % MOD)