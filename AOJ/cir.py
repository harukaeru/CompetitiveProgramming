import sys

s = list(input().replace('\n', ''))
p = list(input().replace('\n', ''))

ext_s = s + s

for i in range(len(s)):
    x = i
    for j, p_s in enumerate(p):
        if ext_s[x] != p_s:
            break
        elif ext_s[x] == p_s:
            x += 1

        if j == len(p) - 1:
            print('Yes')
            exit()
print('No')
