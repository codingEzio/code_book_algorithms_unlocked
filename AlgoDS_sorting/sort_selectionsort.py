from utils.annotated_types import IntList


class Solution:
    def selection_sort(self, nums: IntList) -> IntList:
        """
        Requirements: Integer list AND sorted by ASC

        The outer loop tries to compare one element with every other
        elements. When the comparison is done, move it out of our way,
        which means directly switching the position (move the smallest
        to the front), then we compare the element after it along with
        the element after the elements after the "new" base element to
        compare.
        """
        length = len(nums)

        if length == 0:
            return []

        for asc_left in range(0, length - 1):
            # since we're sorting in ascending order, if the left is the
            # the smaller one, we'll keep it that way (like a default).
            smallest = asc_left

            for asc_right in range(asc_left + 1, length):

                # if we didn't see the default (left is smaller), switch
                # the position ('smallest' underneah is still the left)
                if nums[smallest] > nums[asc_right]:
                    smallest = asc_right

            # finished comparing the base element with every other elements
            # if the left is indeed smaller, we'll just go to the next loop,
            # if it isn't, move the smaller one to the front (also kind move
            # it out of our way for the comparisons for the remaining elements
            if smallest != asc_left:
                nums[smallest], nums[asc_left] = nums[asc_left], nums[smallest]

        return nums


if __name__ == "__main__":
    E = {
        "c1": {"in": [-1, -20, 9, 5], "out": [-20, -1, 5, 9]},
        "c2": {"in": [-5, -2, -1, 4], "out": [-5, -2, -1, 4]},
        "c3": {"in": [0], "out": [0]},
    }

    run = Solution()

    assert run.selection_sort(E["c1"]["in"]) == E["c1"]["out"]
    assert run.selection_sort(E["c2"]["in"]) == E["c2"]["out"]
    assert run.selection_sort(E["c3"]["in"]) == E["c3"]["out"]
