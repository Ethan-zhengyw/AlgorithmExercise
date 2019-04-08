def shell_sort(array):
    length = len(array)
    gap = length / 2

    # loop until gap equals to 1
    while gap > 0:

        # remember step one by one
        for i in range(0, length - gap):
            # elements before array[i] are sorted(with certain gap)
            # need to select the correct position for array[i + gap]
            end = i + gap

            while end - gap >= 0 and array[end - gap] > array[end]:
                array[end], array[end - gap] = array[end - gap], array[end]
                end -= gap

        gap /= 2


def shell_sort_2(array):
    length = len(array)
    gap = length / 2

    # loop until gap equals to 1
    while gap > 0:

        # remember step one by one
        for i in range(gap, length):
            # elements before array[i] are sorted(with certain gap)
            # need to select the correct position for array[i + gap]
            pre = i - gap
            tmp = array[i]

            while pre >= 0 and array[pre] > tmp:
                array[pre + gap] = array[pre]
                pre -= gap

            array[pre + gap] = tmp

        gap /= 2
