from collections import defaultdict

from annotated_types import IntList
from utils import randomize


def counting_sort(arr: IntList, min_el: int, max_el: int) -> IntList:
    """An implementation of counting sort.
    The input to be sorted is assumed to be simply a sequence of integers,
    or serves as a subroutine for other algorithms (e.g. radix sort).

    As its name suggests, each of the element was given an 'count',
    for the duplicated ones, it simply do "*" on it.
    """
    count = defaultdict(int)
    for i in arr:
        count[i] += 1

    result = []
    for j in range(min_el, max_el + 1):
        result += [j] * count[j]

    return result


if __name__ == "__main__":
    inputs: IntList = [6, 9, 7, 8, 4, 5, 10]
    sorted_inputs: IntList = [4, 5, 6, 7, 8, 9, 10]

    randomize(inputs)
    min_el, max_el = min(inputs), max(inputs)
    assert (
        counting_sort(arr=inputs, min_el=min_el, max_el=max_el)
        == sorted_inputs
    )
