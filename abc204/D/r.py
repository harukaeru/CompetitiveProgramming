import random

def r(x):
    return random.randint(1, x)

def r2(x):
    return random.randint(2, x)

N = r2(10)
print(N)
a = []
for i in range(N):
    a.append(r(10))
print(' '.join(map(str, a)))
