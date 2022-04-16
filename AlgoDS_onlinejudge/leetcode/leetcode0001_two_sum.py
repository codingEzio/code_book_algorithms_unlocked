# Status
#   core
#       solved by myself        : yes
#       submitted to leetcode   : yes
#   experiment
#       self-contained (stdlib) : yes
#       runnable locally        : yes


def two_sum(nums_arr, target):
    if len(nums_arr) <= 1:
        return []

    dict_item_as_key = dict()

    for idx, item in enumerate(nums_arr):
        remainder = target - item

        if remainder in dict_item_as_key:
            return [dict_item_as_key[remainder], idx]
        else:
            dict_item_as_key[item] = idx


assert two_sum([9, 3, 7, 1], 10) == [1, 2]
assert two_sum([9, 1, 9, 1], 10) == [0, 1]
assert two_sum([10], 10) == []
assert two_sum([], 10) == []
