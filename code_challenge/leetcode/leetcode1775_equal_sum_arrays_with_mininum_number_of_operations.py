# Status
#   core
#       solved by myself        : not yet
#       submitted to leetcode   : not yet
#   experiment
#       self-contained (stdlib) : yes
#       runnable locally        : yes
from typing import List
from collections import Counter


def min_operations(nums1: List[int], nums2: List[int]) -> int:
    """
    https://leetcode.com/problems/equal-sum-arrays-with-minimum-number-of-operations/discuss/1085880/Python-O(n)-time-O(1)-space-Greedy
    """
    # 6 elements * 6 < 37 elements
    # 37 elements    > 6 elements * 6
    if len(nums1) * 6 < len(nums2) or len(nums1) > len(nums2) * 6:
        return -1

    # set a explicit rule:
    #   only performing ADD on nums1 (smaller)
    #   only performing SUB on nums2 (larger)
    diff = sum(nums2) - sum(nums1)

    # retain the relationship between them (+/- specific)
    if diff < 0:
        nums1, nums2 = nums2, nums1
        diff = -diff

    # not occurrences, but what num to add for each arrays
    # the Counter remembers the insertions order (changes in python3.7)
    count = Counter(6 - item for item in nums1)
    count += Counter(item - 1 for item in nums2)

    result = 0

    # check the occurrences for each (5, 4, 3, 2, 1), except 6!
    for numtoadd in reversed(range(1, 6)):

        # if (5/4/3/2/1) doesn't exist in either (nums1, nums2), next loop
        if not count[numtoadd]:
            continue

        cnt = min(
            count[numtoadd],
            (diff + numtoadd - 1) // numtoadd,
        )
        result += cnt

        diff -= numtoadd * cnt
        if diff <= 0:
            break

    return result


a1, a2 = [4, 3, 1, 6], [1, 4, 2, 2, 3, 4]
min_operations(a1, a2)
# assert min_operations(a1, a2) == 3
