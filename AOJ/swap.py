import sys

for i, line in enumerate(sys.stdin):
    a, b, c = [int(n) for n in line.replace('\n', '').split(' ')]

    count = 0
    for i in range(a, b + 1):
        if c % i == 0:
            count += 1
    print(count)
