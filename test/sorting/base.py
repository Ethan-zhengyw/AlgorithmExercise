import unittest
import random
import time
from abc import abstractmethod, ABCMeta


class TestSortBase:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_sort_class(self):
        pass

    def check(self, array, array_expected):
        local_time = time.time()
        self.get_sort_class().sort(array)
        print '[%s], size [%s], run time is\t %.10f\n' \
              % (self.get_sort_class().__name__, len(array), time.time() - local_time)
        self.assertEqual(array_expected, array)

    def test_array_empty(self):
        array = []
        array_expected = []
        self.check(array, array_expected)

    def test_array_one(self):
        array = [0]
        array_expected = [0]
        self.check(array, array_expected)

    def test_array_two(self):
        array = [1, 0]
        array_expected = [0, 1]
        self.check(array, array_expected)

    def test_array_three(self):
        array = [1, 2, 0]
        array_expected = [0, 1, 2]
        self.check(array, array_expected)

    def test_array_complicate(self):
        array = [9, 5, 3, 7, 12, 79, 21, 4, 6, 12, 45]
        array_expected = [3, 4, 5, 6, 7, 9, 12, 12, 21, 45, 79]
        self.check(array, array_expected)

    def test_array_huge(self):
        array_size = 1000
        array = [random.randint(1, 101) for _ in range(array_size)]
        array_expected = list(array)
        local_time = time.time()
        array_expected.sort()
        print '[%s], size [%s], run time is\t %.10f' \
              % (list.sort.__name__, array_size, time.time() - local_time)
        self.check(array, array_expected)

    def test_array_sorted(self):
        array_size = 1000
        array = [i for i in range(array_size)]
        array_expected = list(array)
        local_time = time.time()
        array_expected.sort()
        print '[%s], size [%s], run time is\t %.10f' \
              % (list.sort.__name__, array_size, time.time() - local_time)
        self.check(array, array_expected)
