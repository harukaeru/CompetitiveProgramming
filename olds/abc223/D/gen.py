import random
def r(n):
    return random.randint(1, n)

N = r(11)
M = r(11)

print(N, M)
for i in range(M):
    print(r(N), r(N))
