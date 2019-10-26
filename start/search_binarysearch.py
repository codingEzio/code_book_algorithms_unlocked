from annotated_types import IntList


# O(lg n) for sorted array
def binary_search(arr: IntList, query: int):
    low: int = 0
    high: int = len(arr) - 1
    while low <= high:
        mid: int = (low + high) // 2
        if arr[mid] > query:
            high = mid - 1  # tightening the left-handed end index
        elif arr[mid] < query:
            low = mid + 1  # tightening the right-handed end index
        else:
            return mid  # the actual index (when the time comes XD)
    return -1  # not found (incr to the point where 'low > high')


# O(lg n) for sorted array
def binary_search_recursive(
    arr: IntList, query: int, low: int = 0, high: int = -1
):
    if len(arr) == 0:
        return -1
    if high == -1:
        high = len(arr) - 1

    if low >= high:
        if arr[low] == query:
            return low
        else:
            return -1

    mid = (low + high) // 2
    if arr[mid] > query:
        return binary_search_recursive(arr, query, low, mid - 1)
    elif arr[mid] < query:
        return binary_search_recursive(arr, query, mid + 1, high)
    else:
        return mid


if __name__ == "__main__":
    inputs: IntList = [3, 4, 5, 6, 7, 8]

    assert binary_search(arr=inputs, query=4) == 1
    assert binary_search(arr=inputs, query=10) == -1

    assert binary_search_recursive(arr=inputs, query=4) == 1
    assert binary_search_recursive(arr=inputs, query=10) == -1
