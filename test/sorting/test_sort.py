import unittest
from base import TestSortBase

import sorting.sort as sort_classes


class TestQuickSort(TestSortBase, unittest.TestCase):
    def get_sort_class(self):
        return sort_classes.QuickSort


class TestInsertionSort(TestSortBase, unittest.TestCase):
    def get_sort_class(self):
        return sort_classes.InsertionSort


class TestMergeSort(TestSortBase, unittest.TestCase):
    def get_sort_class(self):
        return sort_classes.MergeSort


class TestBubbleSort(TestSortBase, unittest.TestCase):
    def get_sort_class(self):
        return sort_classes.BubbleSort


class TestSelectionSort(TestSortBase, unittest.TestCase):
    def get_sort_class(self):
        return sort_classes.SelectionSort


class TestShellSort(TestSortBase, unittest.TestCase):
    def get_sort_class(self):
        return sort_classes.ShellSort


class TestHeapSort(TestSortBase, unittest.TestCase):
    def get_sort_class(self):
        return sort_classes.HeapSort


class TestCountingSort(TestSortBase, unittest.TestCase):
    def get_sort_class(self):
        return sort_classes.CountingSort


class TestBucketSort(TestSortBase, unittest.TestCase):
    def get_sort_class(self):
        return sort_classes.BucketSort


if __name__ == '__main__':
    unittest.main()
