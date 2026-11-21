elements = []
array = []

numbers_set = set()
numbers_list = []

for i in range(3):
    elements.append(int(input()))
    array.append(list(map(int, input().split())))

    for k in range(elements[i]):
        numbers_set.add(array[i][k])

for item in numbers_set:
    j = 0
    for i in range(3):
        if item in array[i]:
            j = j + 1

    if (j >= 2):
        numbers_list.append(item)

numbers_list.sort()
print(*numbers_list)