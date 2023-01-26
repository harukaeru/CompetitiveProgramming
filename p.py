import random
import time

tree = '🌴'
house = '🏡'
car = '🚗'
N = 25

tree_count = random.randint(2, 5)
house_count = random.randint(2, 5)

scene = [tree] * tree_count + [house] * house_count + ['　'] * (N - tree_count - house_count)
random.shuffle(scene)

for i in range(N):
    s = ''
    for j in range(i + N - 1, i - 1, -1):
        if j - i == N // 2:
            s += car
        else:
            s += scene[j % N]

    print(s, end='\r')
    time.sleep(0.1)
