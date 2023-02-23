START = 0
END = 2 ** 3
print(END - START)
for i in range(START, END):
    x = bin(i).replace('0b', '')
    s = '{:>03s}'.format(x)
    print(3)
    print(s)
