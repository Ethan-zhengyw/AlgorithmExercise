def bubble_sort(array):
    for i in range(len(array) - 1):
        swapped = False

        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
                swapped = True

        if not swapped:
            break
