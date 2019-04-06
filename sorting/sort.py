from abc import abstractmethod, ABCMeta
from sorting.quick_sort import quick_sort
from sorting.insertion_sort import insertion_sort_3 as insertion_sort


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
