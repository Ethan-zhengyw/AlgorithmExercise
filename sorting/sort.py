from abc import abstractmethod, ABCMeta
from sorting.quick_sort import quick_sort
from sorting.insertion_sort import insertion_sort_3 as insertion_sort
from sorting.merge_sort import merge_sort
from sorting.bubble_sort import bubble_sort
from sorting.selection_sort import selection_sort
from sorting.shell_sort import shell_sort_2 as shell_sort
from sorting.heap_sort import heap_sort


class Sort:
    __metaclass__ = ABCMeta

    @staticmethod
    @abstractmethod
    def sort(array):
        pass


class QuickSort(Sort):
    @staticmethod
    def sort(array):
        quick_sort(array, 0, len(array) - 1)


class InsertionSort(Sort):
    @staticmethod
    def sort(array):
        insertion_sort(array)


class MergeSort(Sort):
    @staticmethod
    def sort(array):
        merge_sort(array, 0, len(array) - 1)


class BubbleSort(Sort):
    @staticmethod
    def sort(array):
        bubble_sort(array)


class SelectionSort(Sort):
    @staticmethod
    def sort(array):
        selection_sort(array)


class ShellSort(Sort):
    @staticmethod
    def sort(array):
        shell_sort(array)


class HeapSort(Sort):
    @staticmethod
    def sort(array):
        heap_sort(array)
