import random

N = 1000000

d = []
for i in range(N):
    if i == 0:
        d.append(random.randint(1, 10))
    else:
        d.append(random.randint(0, 10))

print(sum(d) % 9)
new_d = int(''.join(map(str, d)))
print(new_d % 9)
