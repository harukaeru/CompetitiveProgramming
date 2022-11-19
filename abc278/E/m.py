import random
H = 300
W = 300
N = 9000
h = 20
w = 20
print(H, W, N, h, w)
for i in range(H):
    x = []
    for j in range(W):
        r = random.randint(1, N)
        x.append(r)
    print(*x)

