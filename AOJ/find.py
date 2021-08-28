import sys

w = input().replace('\n', '').lower()

count = 0
for line in sys.stdin:
    line = line.replace('\n', '').lower()
    if line == 'END_OF_TEXT':
        break

    words = line.split()
    for word in words:
        if w == word:
            count += 1
print(count)
