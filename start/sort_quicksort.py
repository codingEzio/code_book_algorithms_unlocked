from random import choice as pick_random_one

from annotated_types import IntList
from utils import randomize


def quick_sort(arr: IntList) -> IntList:
    """An implementation of quick sort algorithm.
    """
    less: IntList = []
    more: IntList = []
    pivotList: IntList = []

    if len(arr) <= 1:
        return arr
    else:
        pivot: int = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)

        less = quick_sort(less)
        more = quick_sort(more)
        return less + pivotList + more


def quick_sort_rand_pivot(arr: IntList) -> IntList:
    """An implementation of quick sort algorithm.
    This one is a bit different from the 1st one, one of them is that
    the pivot we chosed might be a bit better than the direct `arr[0]`.
    """
    if len(arr) <= 1:
        return arr
    else:
        more: IntList = []
        less: IntList = []
        pivot: int = pick_random_one(arr)

        for i in arr:
            if i < pivot:
                less.append(i)
            if i > pivot:
                more.append(i)
        less = quick_sort_rand_pivot(less)
        more = quick_sort_rand_pivot(more)

        return less + [pivot] * arr.count(pivot) + more


def quick_sort_list_comp(arr: IntList) -> IntList:
    """An implementation of quick sort algorithm using list comprehensions.
    """
    if not arr:
        return []
    else:
        pivot: int = arr[0]
        less = [x for x in arr if x < pivot]
        more = [x for x in arr[1:] if x >= pivot]

        return quick_sort_list_comp(less) \
            + [pivot] \
            + quick_sort_list_comp(more)


if __name__ == "__main__":
    inputs: IntList = [6, 9, 7, 8, 4, 5, 10]
    sorted_inputs: IntList = [4, 5, 6, 7, 8, 9, 10]

    randomize(inputs)
    assert quick_sort(inputs) == sorted_inputs

    randomize(inputs)
    assert quick_sort_rand_pivot(inputs) == sorted_inputs

    randomize(inputs)
    assert quick_sort_list_comp(inputs) == sorted_inputs
