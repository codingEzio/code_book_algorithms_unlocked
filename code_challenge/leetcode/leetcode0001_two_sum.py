from typing import List, Dict


def two_sum(nums: List[int], target: int):
    """
    Giving a list [9, 7, 3, 1, 5] an integer 10,
    it should produce something like [7, 3] (an list of indexes).
    """
    # e.g. []
    num_to_index: Dict[int, int] = {}

    idx: int
    num: int
    for idx, num in enumerate(nums):
        if target - num in num_to_index:
            return [num_to_index[target - num], idx]

        num_to_index[num] = idx

    return []


assert two_sum([9, 7, 3, 1], 10) == [1, 2]  # not 0,3 🤔
assert two_sum([9, 1, 3, 1], 10) == [0, 1]
assert two_sum([9, 2, 3, 1], 10) == [0, 3]
assert two_sum([9, 0, 1], 10) == [0, 2]
assert two_sum([1], 1) == []
