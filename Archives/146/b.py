N = int(input())
S = input().replace('\n', '')

array = [chr(x) for x in range(ord('A'), ord('Z') + 1)]

ans = ''
for s in S:
    index = ord(s) - ord('A')
    ans += array[(index + N) % 26]

print(ans)
