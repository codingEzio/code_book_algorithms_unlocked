from src.annotated_types import (
    IntList
)
from src.test_utils import randomize


def radix_sort(arr, base=10):
    """A simple implementation of radix sort (order: DESC).
    References:
        http://qaru.site/questions/15331230/radix-sort-python-string
    """

    def list_to_buckets(_arr, _base, _iteration):
        buckets = [[] for _ in range(_base)]
        for num in _arr:
            digit = (num // (_base ** _iteration)) % _base
            buckets[digit].append(num)
        return buckets

    def buckets_to_list(buckets):
        numbers = []
        for bucket in buckets:
            for num in bucket:
                numbers.append(num)
        return numbers

    maxval = max(arr)

    iteration = 0
    while base ** iteration <= maxval:
        arr = buckets_to_list(list_to_buckets(arr, base, iteration))
        iteration += 1

    return arr


if __name__ == "__main__":
    inputs: IntList = [6, 9, 7, 8, 4, 5, 10]
    sorted_inputs: IntList = [4, 5, 6, 7, 8, 9, 10]

    randomize(inputs)
    assert radix_sort(inputs) == sorted_inputs
