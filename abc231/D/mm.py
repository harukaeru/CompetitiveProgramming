import random
N = 10
x = list(range(1, N +1))
random.shuffle(x)
# print(x)
print(N, len(x) - 1)
for i in range(len(x) - 1):
    print(x[i], x[i + 1])
