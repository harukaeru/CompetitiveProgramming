# a + b + c + d = 5
from pprint import pprint

combs = []
for i in range(3 ** 4):
    data = []
    k = i
    for j in range(4):
        data.append(k % 3)
        k //= 3

    print(data)
    combs.append(data)

pprint(combs)
