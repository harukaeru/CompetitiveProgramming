import sys

counter = [0] * 26

print('t', ord('t'))
for line in sys.stdin:
    for s in line:
        i = ord(s)
        if ord('A') <= i <= ord('Z'):
            n = i - ord('A')
            counter[n] += 1
        elif ord('a') <= i <= ord('z'):
            n = i - ord('a')
            counter[n] += 1

for i, count in enumerate(counter):
    character = chr(i + ord('a'))
    print(f'{character} : {count}')

