import sys

length = int(sys.stdin.readline())

for line in sys.stdin:
    array = [int(n) for n in line.split(' ')]
    for i in range(length):
        if i == length - 1:
            print(array[length - (i + 1)], end=' ')
        else:
            print(array[length - (i + 1)], end=' ')
    print()
