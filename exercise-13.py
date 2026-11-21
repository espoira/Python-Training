string_1 = input()
string_2 = input()

words_1 = set(string_1)
words_2 = set(string_2)

if (words_1 != words_2):
    print('NO')
else:
    k = 0
    for item in words_1:
        if string_1.count(item) != string_2.count(item):
            print('NO')
            break
        else:
            k = k + 1

    if (k == len(words_1)):
        print('YES')