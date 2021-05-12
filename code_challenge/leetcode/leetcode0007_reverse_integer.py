# Status
#   core
#       solved by myself        : not yet
#       submitted to leetcode   : not yet
#   experiment
#       self-contained (stdlib) : yes
#       runnable locally        : yes
from sys import maxsize as MAXINT


def reverse_integer(num):
    """
    For  321, it should return  123
    For -321, it should return -123
    """
    negative = num < 0
    num = abs(num)
    reversed_num = 0

    while num != 0:
        reversed_num = reversed_num * 10 + num % 10
        num = num // 10

    # Required for leetcode. Doesn't matter for Python itself.
    if reversed_num >= MAXINT - 1:
        return 0

    return reversed_num if not negative else -reversed_num


reverse_integer(-123) == -321
reverse_integer(321) == 123
reverse_integer(0) == 0
reverse_integer(MAXINT) == 0
