amount = int(input())
numbers = list(map(int, input().split()))

calls = int(input())
diapazons = []

for i in range(calls):
    L, R = map (int, input().split())
    diapazons.append([L, R])

count_array = []
numbers.sort()

for j in range(calls):

    left = 0
    right = amount

    while (left < right):

        middle = (left + right) // 2

        if (numbers[middle] < diapazons[j][0]):
            left = middle + 1
        else:
            right = middle

    index_left = left

    left = 0
    right = amount

    while (left < right):

        middle = (left + right) // 2

        if (numbers[middle] > diapazons[j][1]):
            right = middle
        else:
            left = middle + 1

    index_right = right

    count_array.append(index_right - index_left)

print(*count_array)