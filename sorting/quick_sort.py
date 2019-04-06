def median_pivot(array, low, high):
    # select the middle value as pivot
    # from array[low], array[(low + high) / 2), array[high]
    # print "len array:", len(array)
    mid = (low + high) / 2
    # print "low, high, mid:", low, high, mid
    if array[low] > array[mid]:
        array[low], array[mid] = array[mid], array[low]
    if array[low] > array[high]:
        array[low], array[high] = array[high], array[low]
    if array[mid] > array[high]:
        array[mid], array[high] = array[high], array[mid]
    array[mid], array[high] = array[high], array[mid]
    return array[high]


def partition(array, low, high):
    pivot = median_pivot(array, low, high)

    # i is the final pivot position to return,
    # elements on the left of position i, smaller than or equal to pivot, 
    # elements on the right of position i, bigger than pivot
    i = low

    for j in range(low, high):
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i], array[high] = array[high], array[i]
    return i


# Problem:
# 1. performance - cost 2.8293s to sort an array sized 50000
#     current Function [list.sort] run time is	 0.0141959190
#     current Function [quick_sort_2] run time is	 0.0712571144
#     current Function [quick_sort] run time is	 2.8712029457
#
# 2. array size limit - exception "maximum recursion depth exceeded" occur when array size is 100000
#      current Function [list.sort] run time is	 0.0323131084
#      current Function [quick_sort_2] run time is	 0.1668460369
#      current Function [quick_sort] run time is	 "maximum recursion depth exceeded"
#
#    array size limit - exception "maximum recursion depth exceeded" occur when array size is 10000000
#      current Function [sort] run time is	 3.0840051174
#      current Function [quick_sort_2] run time is	 12.2076458931
#      current Function [quick_sort] run time is	 "maximum recursion depth exceeded"
#
# 3. performance - too slow when array sized 1000000 when modify recursion depth limit
#      current Function [sort] run time is	 0.3166019917
#      current Function [quick_sort_2] run time is	 0.8683018684
#      current Function [quick_sort] run time is	do not stop
#
# TODO:
# 1. random select pivot instead of using the last element
# 2. use loop instead of recursion
def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)


def quick_sort_2(array):
    l = len(array)
    if l < 2:
        return array

    pivot = median_pivot(array, 0, l - 1)

    return (quick_sort_2([a for a in array if a < pivot]) +
            [a for a in array if a == pivot] +
            quick_sort_2([a for a in array if a > pivot]))



