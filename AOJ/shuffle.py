import sys

while 1:
    data = input().replace('\n', '')
    if data == '-':
        break

    m = int(input())
    for i in range(m):
        h = int(input())
        data = data[h:] + data[:h]
    print(data)
