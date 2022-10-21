def f(x):
  return x ** 2 - x + 1

def fp(x):
  return 2 * x - 1

alpha = 0.05
X = 1

while fp(X) >= 0.000001:
  X -= alpha * fp(X)
  print(X, f(X))