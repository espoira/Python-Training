dict_words = set(map(str, input().split()))
text_words = list(map(str, input().split()))

for i in range(len(text_words)):
    for j in range(1, len(text_words[i])):
        if (text_words[i][0:j] in dict_words):
            text_words[i] = text_words[i][0:j]
            break

print(' '.join(text_words))