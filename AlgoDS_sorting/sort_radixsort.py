from utils.annotated_types import IntList, NestedIntList
from utils.input_opts import randomize


# util functions for `radix_sort_2nd`.
def radix_get_length(value: int) -> int:
    """Returns the length, in number of digits, of value
    e.g. For 34, it returns 2.
    """
    digit: int

    if value == 0:
        return 1

    digits = 0
    while value != 0:
        digits += 1
        value //= 10

    return digits


# util functions for `radix_sort_2nd`.
def radix_get_max_length(numbers: IntList) -> int:
    """Returns the maximum length, in number of digits, out of all list elements
    e.g. For [30, 9, 111], it returns 3 (aka. 111).
    """
    max_digits: int
    num: int
    digit_count: int

    max_digits = 0

    for num in numbers:
        digit_count = radix_get_length(num)
        if digit_count > max_digits:
            max_digits = digit_count

    return max_digits


# https://derka.space/RefrencePage/DataStructuresZy/SortingAlgorithms/Python_RadixSort/SortingAlgorithms_Python_RadixSort_s14.php
# O(n²)
def radix_sort_2nd(numbers: IntList) -> IntList:
    """Yet another implementation on radix sort (more understandable IMHO).
    """
    pow_10: int
    max_digits: int
    num: int
    bucket_index: int
    bucket: IntList
    buckets: NestedIntList
    negatives: IntList
    non_negatives: IntList

    buckets = []
    for _ in range(10):
        buckets.append([])

    pow_10 = 1
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
# O(n²)
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
    inputs: IntList = [63, 931, 7, 18, 4, 5, 10]
    sorted_inputs: IntList = [4, 5, 7, 10, 18, 63, 931]

    randomize(inputs)
    assert radix_sort(inputs) == sorted_inputs

    randomize(inputs)
    radix_sort_2nd(inputs)
    assert inputs == sorted_inputs
