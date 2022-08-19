import random

def r():
    return random.randint(1, 10)

def rN():
    return random.randint(1, N)

def mr():
    return random.randint(-100, 100)

N = r()
K = N - (rN() - 1)

row = f'{N} {K}'
row2 = ' '.join(map(str, [mr() for s in range(N)]))


print(row)
print(row2)
