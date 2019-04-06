def insertion_sort(array):
    # i is length of sorted array
    for i in range(1, len(array)):

        # element to insert into sorted array
        curr = array[i]

        # find the correct position for curr
        for j in range(i - 1, -1, -1):
            if array[j] > curr:
                array[j + 1] = array[j]
            else:
                # Warning:
                # There are two case to leave current loop
                # 1. without enter else: j will minus 1 once more times
                # 2. enter else
                j = j + 1
                break

        array[j] = curr


# version more easy to understand
def insertion_sort_2(array):
    # i is length of sorted array
    for i in range(1, len(array)):

        # element to insert into sorted array
        curr = array[i]
        is_curr_set = False

        # find the correct position for curr
        for j in range(i - 1, -1, -1):
            if array[j] > curr:
                array[j + 1] = array[j]
            else:
                # Warning:
                # There are two case to leave current loop
                # 1. without enter else: j will minus 1 once more times
                # 2. enter else
                array[j + 1] = curr
                is_curr_set = True
                break

        if not is_curr_set:
            # j must be 0
            array[j] = curr


# version more easy to understand
def insertion_sort_3(array):
    # i is length of sorted array
    for i in range(1, len(array)):

        # element to insert into sorted array
        curr = array[i]

        # find the correct position for curr
        j = i - 1  # j + 1 is the final position
        while j >= 0 and array[j] > curr:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = curr
