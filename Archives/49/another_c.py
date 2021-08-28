reversed_S = input().replace('\n', '')[::-1]

words = list(map(lambda a: a[::-1], ['dream', 'dreamer', 'erase', 'eraser']))

while 1:
    is_word_match = False
    for word in words:
        has_word = reversed_S[:len(word)] == word
        if has_word:
            is_word_match = True
            reversed_S = reversed_S[len(word):]
            if (reversed_S == ''):
                print('YES')
                exit()
            break
    if not is_word_match:
        print('NO')
        exit()
