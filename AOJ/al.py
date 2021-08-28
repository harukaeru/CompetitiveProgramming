import sys

sentences = sys.stdin.readline()

before = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
after = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

for s in sentences:
    try:
        i = before.index(s)
        print(after[i], end='')
    except:
        print(s, end='')
