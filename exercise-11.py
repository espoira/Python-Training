tests = int(input())

counts_array = []
lengths_array = []

for i in range(tests):

    array_length = int(input())
    array = list(map(int, input().split()))

    count = 0
    sequences_len = []

    j = 0
    while (j < array_length):

        count = count + 1
        seq_length = 0

        minimal_element = array_length
        while (minimal_element > seq_length) and (j < array_length):

            if (array[j] <= seq_length):
                break
            else:
                seq_length = seq_length + 1

                if (array[j] < minimal_element):
                    minimal_element = array[j]
                j = j + 1

        sequences_len.append(str(seq_length))

    counts_array.append(count)
    lengths_array.append(" ".join(sequences_len))

for i in range(tests):
    print(counts_array[i])
    print(lengths_array[i])