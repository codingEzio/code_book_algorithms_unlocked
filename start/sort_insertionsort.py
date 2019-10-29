from annotated_types import IntList
import bisect
from random import choices


def randomize_inputs(arr: IntList):
    length: int = len(arr)
    return choices(arr, k=length)


def sort_inputs_by(func_name, arr: IntList):
    return func_name(arr)


# O(n²) typically
def insertion_sort(arr: IntList):
    """The speed of this algorithm is also not that good as well,
    the only thing this algo does is compare the current element with
    the previous elem, then decide swap them or not (I thought it's hard..).
    """

    # I know the names I used here might be a little confusing to you,
    # Umm.. sorry!
    for idx_add1 in range(1, len(arr)):
        val_adi1 = arr[idx_add1]
        idx_orig = idx_add1 - 1
        while idx_orig >= 0 and arr[idx_orig] > val_adi1:
            arr[idx_orig + 1] = arr[idx_orig]
            arr[idx_orig] = val_adi1
            idx_orig = idx_orig - 1
    return arr
    pass


# O(n²) typically
def insertion_sort_bisect(arr: IntList):
    pass


# O(n²) typically
def insertion_sort_binsearch(arr: IntList):
    pass


if __name__ == "__main__":
    inputs: IntList = [6, 7, 8, 3, 4, 5]
    sorted_inputs: IntList = [3, 4, 5, 6, 7, 8]

    assert sort_inputs_by(insertion_sort, arr=inputs) == sorted_inputs
