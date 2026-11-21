threads = int(input())
th_length = list(map(int, input().split()))

sum_lengths = 0
max_length = 1

for i in range(threads):
    sum_lengths = sum_lengths + th_length[i]
    if (th_length[i] > max_length):
        max_length = th_length[i]

if (2*max_length > sum_lengths):
    min_length = 2*max_length - sum_lengths
else:
    min_length = sum_lengths

print(min_length)