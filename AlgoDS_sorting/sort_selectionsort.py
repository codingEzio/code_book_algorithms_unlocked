from utils.annotated_types import IntList


# O(n²) typically
def selection_sort(arr: IntList):
    # 1. e.g. [7,2,3] -> [2,7,3] -> [2,3,7]
    # 2. [..[..[..]]] (0,rest) (1,rest) (push the smallest to the left-side)
    for i, e in enumerate(arr):
        mn: IntList = min(range(i, len(arr)), key=arr.__getitem__)
        arr[i], arr[mn] = arr[mn], e
    return arr


if __name__ == "__main__":
    inputs: IntList = [6, 7, 8, 3, 4, 5]
    assert selection_sort(inputs) == [3, 4, 5, 6, 7, 8]
