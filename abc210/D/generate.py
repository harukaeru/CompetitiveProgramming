import random
def r(n):
    return random.randint(1, n)

H = r(10)
W = r(10)
data = f'{H} {W} {r(1000)}\n'
for i in range(H):
    for j in range(W):
        data += f'{r(10)}'
        if j != W - 1:
            data += ' '
    data += '\n'

print(data)
