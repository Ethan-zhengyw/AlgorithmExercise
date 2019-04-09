def heap_sort(array):
    build_max_heap(array)
    end = len(array) - 1
    while end > 0:
        array[0], array[end] = array[end], array[0]
        end -= 1
        max_heapify(array, 0, end)


# Build a max heap from bottom to top
# by calling max_heapify
def build_max_heap(array):
    end = len(array) - 1
    i = (end - 1) / 2
    while i >= 0:
        max_heapify(array, i, end)
        i -= 1


# recursively fix the max-heap violation of the sub tree
# Time complexity: O(logN)
def max_heapify(array, i, end):
    max_index = i
    left_child_index = 2 * max_index + 1
    right_child_index = 2 * max_index + 2

    if (left_child_index <= end) and (array[left_child_index] > array[i]):
        max_index = left_child_index

    if (right_child_index <= end) and (array[right_child_index] > array[max_index]):
        max_index = right_child_index

    if max_index != i:
        array[i], array[max_index] = array[max_index], array[i]
        max_heapify(array, max_index, end)
