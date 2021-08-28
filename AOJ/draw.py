import sys

patterns = ['#', '.']

for line in sys.stdin:
    a, b = [int(n) for n in line.split(' ')]

    if a == 0 and b == 0:
        exit()

    for i in range(a):
        pattern_idx = i % 2
        for j in range(b):
            print(patterns[pattern_idx], end='')

            pattern_idx = 1 if pattern_idx == 0 else 0
        print()
    print()
