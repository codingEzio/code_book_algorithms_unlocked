from heapq import merge
from collections import deque

from typing import Deque, Union
from annotated_types import IntList
from utils import randomize


def _merge(left: IntList, right: IntList) -> IntList:
    """Native `merge` implementation, used for the recursive
    version of merge sort.
    """
    result: IntList = []
    print(f"I'm in merge -- {result}")

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

    print(f"I'm out merge -- {result} (actually the end)\n")
    return result


def __merge(X: Union[IntList, Deque], Y: Union[IntList, Deque]) -> IntList:
    """Native `merge` implementation, used for the non-recursive
    version of merge sort.
    """
    X, Y, Z = deque(X), deque(Y), []
    while len(X) > 0 and len(Y) > 0:
        if X[0] < Y[0]:
            Z.append(X.popleft())
        else:
            Z.append(Y.popleft())
    return Z + list(X) + list(Y)


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


def merge_sort_native(arr: IntList) -> IntList:
    """Merge sort based on native `merge` implementation.
    """
    if len(arr) <= 1:
        return arr

    mid: int = len(arr) // 2
    left: IntList = arr[:mid]
    right: IntList = arr[mid:]

    print(f"I'm in main sort LEFT -- {left}")
    print(f"I'm in main sort RIGHT -- {right}")
    left = merge_sort_native(left)
    right = merge_sort_native(right)

    print(f"I'm out main sort -- {left}, {right} (head to merge!)")
    return list(_merge(left, right))


def merge_sort_no_recursion(arr: IntList) -> IntList:
    """A non-recursive version of merge sort (hell yeah!).
    References (first time know this -> intro -> implementation)
    1. https://stackoverflow.com/questions/1557894/non-recursive-merge-sort/#1557919
    2. https://www.algorithmist.com/index.php/Merge_sort#Bottom-up_merge_sort
    3. https://www.quora.com/What-is-the-difference-between-top-down-merge-sort-and-bottom-up-merge-sort
    """
    if len(arr) <= 1:
        return list(arr)
    Q = deque([elem] for elem in arr)
    while True:
        X = Q.popleft()
        if len(Q) == 0:
            return X
        Y = Q.popleft()
        Q.append(__merge(X, Y))


if __name__ == "__main__":
    inputs: IntList = [6, 7, 8, 4, 5, 2, 3]
    sorted_inputs: IntList = [2, 3, 4, 5, 6, 7, 8]

    # The recursive part is best explained here
    # https://stackoverflow.com/questions/10502533/explanation-of-merge-sort-for-dummies/#10503273

    randomize(inputs)
    assert merge_sort_heapq(inputs) == sorted_inputs

    randomize(inputs)
    assert merge_sort_native(inputs) == sorted_inputs

    randomize(inputs)
    assert merge_sort_no_recursion(inputs) == sorted_inputs
