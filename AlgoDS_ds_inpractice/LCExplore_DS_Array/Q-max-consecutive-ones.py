"""
https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3238/

Given a binary array nums (aka. only 0 and 1), return the maximum of
number of consecutive 1s in the array.

Example:
    Input: [1,1,0,1,1,1]    -> Output: 3
    Input: [1,0,1,1,0,1]    -> Output: 2
"""


class Solution:
    def max_consec_ones(self, nums) -> int:
        counter = 0
        ans = 0

        for i in nums:
            if i == 1:
                counter += 1

                if ans < counter:
                    ans = counter
            else:
                counter = 0

        return ans


if __name__ == "__main__":
    run = Solution()
    nums = [1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1]

    assert run.max_consec_ones(nums) == 5
