from src.annotated_types import IntList, NestedIntList
from src.test_utils import randomize


# util functions for `radix_sort_2nd`.
def radix_get_length(value: int) -> int:
    """# Returns the length, in number of digits, of value
    """
    if value == 0:
        return 1

    digits: int = 0
    while value != 0:
        digits += 1
        value //= 10

    return digits


# util functions for `radix_sort_2nd`.
def radix_get_max_length(numbers: IntList) -> int:
    """Returns the maximum length, in number of digits, out of all list elements
    """
    max_digits: int = 0
    num: int

    for num in numbers:
        digit_count: int = radix_get_length(num)
        if digit_count > max_digits:
            max_digits = digit_count

    return max_digits


# https://derka.space/RefrencePage/DataStructuresZy/SortingAlgorithms/Python_RadixSort/SortingAlgorithms_Python_RadixSort_s14.php
def radix_sort_2nd(numbers: IntList) -> IntList:
    """Yet another implementation on radix sort.
    """
    buckets: NestedIntList
    max_digits: int
    num: int
    pow_10: int = 1
    bucket_index: int
    bucket: IntList
    negatives: IntList
    non_negatives: IntList

    buckets = [[] * 10]
    max_digits = radix_get_max_length(numbers)

    for digit_index in range(max_digits):
        for num in numbers:
            bucket_index = (num // pow_10) % 10
            buckets[bucket_index].append(num)

        numbers.clear()

        for bucket in buckets:
            numbers.extend(bucket)
            bucket.clear()

        pow_10 = pow_10 * 10

    negatives = []
    non_negatives = []
    for num in numbers:
        if num < 0:
            negatives.append(num)
        else:
            non_negatives.append(num)

    negatives.reverse()
    numbers.clear()
    numbers.extend(negatives + non_negatives)

    return numbers


# http://qaru.site/questions/15331230/radix-sort-python-string
def radix_sort(arr: IntList, base=10):
    """A simple implementation of radix sort (order: DESC).
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
