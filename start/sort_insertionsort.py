from annotated_types import IntList


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
        while idx_orig >= 0 and val_adi1 < arr[idx_orig]:
            arr[idx_orig+1] = arr[idx_orig]
            arr[idx_orig] = val_adi1
            idx_orig = idx_orig - 1
    return arr


if __name__ == "__main__":
    inputs: IntList = [6, 7, 8, 3, 4, 5]
    sorted_inputs: IntList = insertion_sort([6, 7, 8, 3, 4, 5])
    assert insertion_sort(inputs) == sorted_inputs
