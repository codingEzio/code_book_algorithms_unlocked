# Status
#   core
#       solved by myself        : yes
#       submitted to leetcode   : yes
#   experiment
#       self-contained (stdlib) : yes
#       runnable locally        : not yet


class Solution:
    """
    a1, a2 .. b1, b2 .. -> a1, b1, a2, b2 ..
    """

    def shuffle(self, arr, n_pairs):
        divide_line = operations_needed = len(arr) // 2
        arr_x, arr_y = arr[:divide_line], arr[divide_line:]
        insert_starting_index = 1

        for idx in range(operations_needed):
            arr_x.insert(insert_starting_index, arr_y[idx])

            insert_starting_index += 2

        return arr_x
