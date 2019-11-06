import bisect

from utils.annotated_types import IntList
from utils.input_opts import randomize, sort_inplace


# O(n²) typically
def insertion_sort(arr: IntList) -> IntList:
    """The speed of this algorithm is also not that good as well,
    the only thing this algo does is compare the current element with
    the previous elem, then decide swap them or not (I thought it's hard..).
    """

    # I know the names I used here might be a little confusing to you,
    # Umm.. sorry!
    idx_add1: int
    for idx_add1 in range(1, len(arr)):
        val_adi1 = arr[idx_add1]
        idx_orig = idx_add1 - 1
        while idx_orig >= 0 and arr[idx_orig] > val_adi1:
            arr[idx_orig + 1] = arr[idx_orig]
            arr[idx_orig] = val_adi1
            idx_orig = idx_orig - 1
    return arr


# O(n²) typically
def insertion_sort_bis(arr: IntList) -> None:
    """Same logic, compare the current with previous one,
    but using the built-in binary search algorithm :)
    """
    idx: int
    for idx in range(1, len(arr)):
        bisect.insort(arr, arr.pop(idx), 0, idx)


# O(n²) typically
def insertion_sort_bin(arr: IntList) -> None:
    idx: int
    for idx in range(1, len(arr)):
        key = arr[idx]
        low, high = 0, idx
        while high > low:
            mid = (low + high) // 2
            if arr[mid] < key:
                low = mid + 1
            else:
                high = mid
        arr[:] = arr[:low] + [key] + arr[low:idx] + arr[idx + 1:]


if __name__ == "__main__":
    inputs: IntList = [6, 7, 8, 3, 4, 5]
    sorted_inputs: IntList = [3, 4, 5, 6, 7, 8]

    randomize(inputs)
    assert insertion_sort(arr=inputs) == sorted_inputs

    randomize(inputs)
    sort_inplace(func=insertion_sort_bis, arr=inputs)
    assert inputs == sorted_inputs

    randomize(inputs)
    sort_inplace(func=insertion_sort_bin, arr=inputs)
    assert inputs == sorted_inputs
