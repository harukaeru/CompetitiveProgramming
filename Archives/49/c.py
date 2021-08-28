S = input().replace('\n', '')

# def search(string):
#     if string == '':
#         print('YES')
#         exit()
#
#     for word in ['dream', 'dreamer', 'erase', 'eraser']:
#
#         has_word = string[:len(word)] == word
#
#         if has_word:
#             next_string = string[len(word):]
#             search(next_string)
#         continue
#
# search(S)
# print('NO')

n = len(S) / len('erase')

T = ['']
i = 0
while i < n:
    next_words = []
    for t in T:
        for word in ['dream', 'dreamer', 'erase', 'eraser']:
            next_word = t + word
            has_next_word = S[:len(next_word)] == next_word

            if S == next_word:
                exit()

            if has_next_word:
                next_words.append(next_word)
    T = next_words
    i += 1

print('NO')
