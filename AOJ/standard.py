import math

while 1:
    n = int(input())
    if n == 0:
        exit()

    students = list(map(int, input().split()))
    total = 0
    for s in students:
        total += s
    average = total / n

    dev_total = 0
    for s in students:
        ds = s - average
        dev_total += ds ** 2

    dev_average = dev_total / n
    print(math.sqrt(dev_average))
