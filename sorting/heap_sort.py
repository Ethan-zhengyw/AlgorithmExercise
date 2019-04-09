def heap_sort(array):
    end = len(array) - 1
    while end > 0:
        build_max_heap(array, end)
        array[0], array[end] = array[end], array[0]
        end -= 1


def build_max_heap(array, end):
    while not is_max_heap(array, end):
        max_heapify(array, end)


def is_max_heap(array, end):
    i = end / 2
    result = True

    while i >= 0:
        left_child_index = 2 * i + 1
        right_child_index = 2 * i + 2

        if (left_child_index <= end) and (array[left_child_index] > array[i]) or \
                (right_child_index <= end) and (array[right_child_index] > array[i]):
            result = False
            break
        i -= 1

    return result


def max_heapify(array, end):
    i = end / 2

    while i >= 0:

        left_child_index = 2 * i + 1
        right_child_index = 2 * i + 2

        if (left_child_index <= end) and (array[left_child_index] > array[i]):
            array[left_child_index], array[i] = array[i], array[left_child_index]

        if (right_child_index <= end) and (array[right_child_index] > array[i]):
            array[right_child_index], array[i] = array[i], array[right_child_index]

        i -= 1
