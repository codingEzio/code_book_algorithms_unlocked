from utils.annotated_types import IntList


# O(n) whatever it has been sorted or not
def linear_search(arr: IntList, query: int) -> int:
    """Return index if given number is found in the list.
    """
    arr_len: int = len(arr)
    for idx in range(arr_len):
        if arr[idx] == query:
            return idx
    return -1


# O(n) whatever it has been sorted or not
def linear_search_sentinel(arr: IntList, query: int) -> int:
    """Return index if given number is found in the list.

    It reduces one comparison in every iterations. In the
    original one we "loop & compare the for-cond & param",
    on this one we only need to "compare the param (& incr).
    """
    arr_len: int = len(arr)  # e.g. [3, 5, 1, 9] => 4
    last: int = arr[-1]  # last=9
    arr[-1] = query  # e.g. search '1' -> arr[-1]=1

    idx: int = 0
    while arr[idx] != query:  # arr[0,1,2,3] ?= 1
        idx += 1  # search 1 => idx=2

    arr[-1] = last  # arr[-1]=9 (the original val)

    # ff->f, otherwise returns True
    # * (idx < arr_len - 1)         -> found(->indx), notfound(false)
    # * (query == arr[arr_len - 1]) -> out of first cond (idx is fine)
    if (idx < arr_len - 1) or (query == arr[-1]):
        # either (1)not found, big index (2)not at the last => f,f => f
        # or (idx<..)  that means it isn't at the last one
        # or (query..) that means it is at the last one (restored bf we cmp)
        return idx
    else:
        return -1


# O(n) whatever it has been sorted or not
def linear_search_foundornot(arr: IntList, query: int) -> bool:
    """Return True if given number is found in the list
    """
    position: int = 0
    found: bool = False
    while position < len(arr) and not found:
        if arr[position] == query:
            found = True
        position += 1
    return found


if __name__ == "__main__":
    arr: IntList = [3, 7, -1, 20]

    assert linear_search(arr=arr, query=-1) == 2
    assert linear_search(arr=arr, query=10) == -1

    assert linear_search_sentinel(arr=arr, query=-1) == 2
    assert linear_search_sentinel(arr=arr, query=10) == -1

    assert linear_search_foundornot(arr=arr, query=-1) is True
    assert linear_search_foundornot(arr=arr, query=10) is False
