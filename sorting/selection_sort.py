def selection_sort(array):
    for i in range(len(array) - 1):
        smallest_index = i
        for j in range(i, len(array)):
            if array[j] < array[smallest_index]:
                smallest_index = j
        array[i], array[smallest_index] = array[smallest_index], array[i]
