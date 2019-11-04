from src.annotated_types import IntList, NestedIntList
from src.test_utils import randomize


def radix_sort(arr: IntList, base=10):
    """A simple implementation of radix sort (order: DESC).
    References:
        http://qaru.site/questions/15331230/radix-sort-python-string
    """

    def list_to_buckets(_arr: IntList, _base: int, _iteration: int):
        buckets: NestedIntList = [[] for _ in range(_base)]
        for num in _arr:
            digit: int = (num // (_base ** _iteration)) % _base
            buckets[digit].append(num)
        return buckets

    def buckets_to_list(buckets):
        numbers: IntList = []

        bucket: IntList
        num: int
        for bucket in buckets:
            for num in bucket:
                numbers.append(num)
        return numbers

    maxval: int = max(arr)

    iteration: int = 0
    while base ** iteration <= maxval:
        arr = buckets_to_list(list_to_buckets(arr, base, iteration))
        iteration += 1

    return arr


if __name__ == "__main__":
    inputs: IntList = [6, 9, 7, 8, 4, 5, 10]
    sorted_inputs: IntList = [4, 5, 6, 7, 8, 9, 10]

    randomize(inputs)
    assert radix_sort(inputs) == sorted_inputs
