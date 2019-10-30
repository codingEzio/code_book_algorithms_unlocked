from heapq import merge
from annotated_types import IntList
from utils import randomize


def merge_sort_heapq(arr: IntList) -> IntList:
    """Merge sort based on `heapq.merge`.
    """
    if len(arr) <= 1:
        return arr

    mid: int = len(arr) // 2
    left_arr: IntList = arr[:mid]
    right_arr: IntList = arr[mid:]

    left_arr = merge_sort_heapq(left_arr)
    right_arr = merge_sort_heapq(right_arr)

    return list(merge(left_arr, right_arr))


if __name__ == "__main__":
    inputs: IntList = [6, 7, 8, 4, 5]
    sorted_inputs: IntList = [4, 5, 6, 7, 8]

    randomize(inputs)
    assert merge_sort_heapq(inputs) == sorted_inputs
