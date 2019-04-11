from insertion_sort import insertion_sort_3 as sort


def bucket_sort(array):
    if not array:
        return

    bucket_num = 50
    minimum = min(array)
    maximum = max(array)
    distance = (maximum - minimum + 1) / (bucket_num - 1)

    buckets = [[] for _ in range(bucket_num + 1)]

    for n in array:
        if distance == 0:
            buckets[0].append(n)
        else:
            buckets[(n - minimum) / distance].append(n)

    i = 0
    for bucket in buckets:
        sort(bucket)
        for n in bucket:
            array[i] = n
            i += 1
