def counting_sort(array):
    size = len(array)

    if size < 2:
        return

    maximum = array[0]

    # find min/max number
    for n in array:
        maximum = n if n > maximum else maximum

    # initialize count array, length maximum + 1
    count = [0 for _ in range(maximum + 1)]

    # build count array
    for i in range(size):
        count[array[i]] += 1

    # convert count array to sum count array
    for i in range(1, maximum + 1):
        count[i] += count[i - 1]

    # tmp array for hold element from original array
    tmp_array = [0 for _ in array]
    for n in array:
        tmp_array[count[n] - 1] = n
        count[n] -= 1

    # copy the result array to the original array
    for i in range(size):
        array[i] = tmp_array[i]
