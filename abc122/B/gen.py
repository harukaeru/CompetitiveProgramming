import random

r = random.randint(1, 10)

for i in range(r):
    print(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), end='')
