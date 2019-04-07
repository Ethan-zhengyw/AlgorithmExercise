def merge(array, left, mid, right):
    result = []
    i, j = left, mid + 1

    while i <= mid and j <= right:
        if array[i] <= array[j]:
            result.append(array[i])
            i += 1
        else:
            result.append(array[j])
            j += 1

    while i <= mid:
        result.append(array[i])
        i += 1

    while j <= right:
        result.append(array[j])
        j += 1

    # or we can copy element in two temp arrays
    # and append the smaller element to original array while comparing
    for i in range(len(result)):
        array[left + i] = result[i]


def merge_sort(array, left, right):
    if left < right:
        mid = (left + right) / 2
        merge_sort(array, left, mid)
        merge_sort(array, mid + 1, right)
        merge(array, left, mid, right)
