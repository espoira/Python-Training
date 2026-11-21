number = int(input())

left = 0
right = number

while (left < right):

    middle = (left + right + 1) // 2

    if (2 * number + middle > middle**2):
        left = middle
    else:
        right = middle - 1

diag_number = left

sum_prev_diag = diag_number * (diag_number - 1) // 2

chisl = ((diag_number + 1) % 2) * (diag_number + 1) + (number - sum_prev_diag) * (-1)**(diag_number + 1)
znamen = (diag_number % 2) * (diag_number + 1) + (number - sum_prev_diag) * (-1)**(diag_number)

print('/'.join([str(chisl), str(znamen)]))