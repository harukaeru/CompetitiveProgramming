import os
import time
import random

def print(*args):
    s = ' '.join(map(str, args)) + '\n'
    f.write(s)

for i in range(100):
    f = open(f'{i}.txt', 'w')
    N = 10
    x = list(range(1, N + 1))
    random.shuffle(x)
    # print(x)
    print(N, len(x) - 1)
    for i in range(len(x) - 1):
        print(x[i], x[i + 1])
    f.close()
    os.system(f'cat {i}.txt | python3 main.py')
