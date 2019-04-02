import unittest
import random
import time
import quick_sort as qs


class TestQuickSort(unittest.TestCase):

    def check_quick_sort(self, array, array_expected):
        local_time = time.time()
        array_sorted = qs.quick_sort_2(array)
        print 'current Function [%s] run time is\t %.10f' % (qs.quick_sort_2.__name__, time.time() - local_time)
        self.assertEqual(array_sorted, array_expected)

        local_time = time.time()
        qs.quick_sort(array, 0, len(array) - 1)
        print 'current Function [%s] run time is\t %.10f\n' % (qs.quick_sort.__name__, time.time() - local_time)
        self.assertEqual(array, array_expected)

    def test_array_empty(self):
        array = []
        array_expected = []
        self.check_quick_sort(array, array_expected)

    def test_array_one(self):
        array = [0]
        array_expected = [0]
        self.check_quick_sort(array, array_expected)

    def test_array_two(self):
        array = [1, 0]
        array_expected = [0, 1]
        self.check_quick_sort(array, array_expected)

    def test_array_three(self):
        array = [1, 2, 0]
        array_expected = [0, 1, 2]
        self.check_quick_sort(array, array_expected)

    def test_array_complicate(self):
        array = [9, 5, 3, 7, 12, 79, 21, 4, 6, 12, 45]
        array_expected = [3, 4, 5, 6, 7, 9, 12, 12, 21, 45, 79]
        self.check_quick_sort(array, array_expected)

    def test_array_huge(self):
        array_size = 10000000
        array = [random.randint(1, 101) for _ in range(array_size)]
        array_expected = list(array)
        local_time = time.time()
        array_expected.sort()
        print 'current Function [%s] run time is\t %.10f' % (list.sort.__name__, time.time() - local_time)
        self.check_quick_sort(array, array_expected)

    def test_array_sorted(self):
        array_size = 1000
        array = [i for i in range(array_size)]
        array_expected = list(array)
        local_time = time.time()
        array_expected.sort()
        print 'current Function [%s] run time is\t %.10f' % (list.sort.__name__, time.time() - local_time)
        self.check_quick_sort(array, array_expected)


if __name__ == '__main__':
    unittest.main()
