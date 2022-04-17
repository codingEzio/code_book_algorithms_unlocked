"""
https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3237/

Given an array of integers, return how many of them contain
an even number of digits.
"""
E = {
    "c1": {"in": [11, 2, 9, 20, 666], "out": 2},
    "c2": {"in": [10, 20, 30, 6, 6, 6], "out": 3},
    "c3": {"in": [7, 7, 7, 7, 1, 1, 1, 44], "out": 1},
}


class Solution:
    def even_num_digits(self, nums) -> int:
        counter = 0

        for elem in nums:
            if len(str(elem)) % 2 == 0:
                counter += 1

        return counter


if __name__ == "__main__":
    run = Solution()

    assert run.even_num_digits(E["c1"]["in"]) == E["c1"]["out"]
    assert run.even_num_digits(E["c2"]["in"]) == E["c2"]["out"]
    assert run.even_num_digits(E["c3"]["in"]) == E["c3"]["out"]
