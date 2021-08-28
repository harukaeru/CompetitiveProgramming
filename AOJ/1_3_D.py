import sys

for i, line in enumerate(sys.stdin):
    a, b = [int(n) for n in line.replace('\n', '').split(' ')]
    if a == 0 and b == 0:
        exit()

    if a > b:
        a, b = b, a
    print(a, b)
