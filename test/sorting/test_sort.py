import unittest
from base import TestSortBase

import sorting.sort as sort_classes


class TestQuickSort(TestSortBase, unittest.TestCase):
    def get_sort_class(self):
        return sort_classes.QuickSort


class TestInsertionSort(TestSortBase, unittest.TestCase):
    def get_sort_class(self):
        return sort_classes.InsertionSort


if __name__ == '__main__':
    unittest.main()
