from random import randint

N = randint(1, 5)
K = randint(1, 10)
A = ' '.join(map(str, [randint(1, 10) for i in range(N)]))
print(N, K)
print(A)
