word = input().replace('\n', '')
q = int(input())

for i in range(q):
    command, *queries = input().replace('\n', '').split()
    if command == 'replace':
        a, b, c = queries
        a, b = int(a), int(b) + 1
        word = word[:a] + c + word[b:]
    elif command == 'reverse':
        a, b = queries
        a, b = int(a), int(b) + 1
        word = word[:a] + word[a:b][::-1] + word[b:]
    elif command == 'print':
        a, b = queries
        a, b = int(a), int(b) + 1
        print(word[a:b])
