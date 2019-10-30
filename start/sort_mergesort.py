from heapq import merge
from annotated_types import IntList
from utils import randomize


def _merge(left: IntList, right: IntList) -> IntList:
    result: IntList = []

    left_idx: int
    right_idx: int
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    if left_idx < len(left):
        result.extend(left[left_idx:])
    if right_idx < len(right):
        result.extend(right[right_idx:])

    return result


def merge_sort_native(arr: IntList) -> IntList:
    """Merge sort based on native `merge` implementation.
    """
    if len(arr) <= 1:
        return arr

    mid: int = len(arr) // 2
    left: IntList = arr[:mid]
    right: IntList = arr[mid:]

    left = merge_sort_native(left)
    right = merge_sort_native(right)

    return list(_merge(left, right))


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

    randomize(inputs)
    assert merge_sort_native(inputs) == sorted_inputs
