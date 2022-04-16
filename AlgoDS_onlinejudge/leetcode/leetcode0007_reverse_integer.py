# Status
#   core
#       solved by myself        : yes
#       submitted to leetcode   : yes
#   experiment
#       self-contained (stdlib) : yes
#       runnable locally        : yes


def check_overflow(x):
    if (-(2 ** 32) <= x <= 2 ** 32 + 1) is False:
        return 0
    else:
        return x


def reverse_integer(x):
    x_as_str_reversed = str(x)[::-1]

    if x_as_str_reversed[-1] == "-":
        x_as_str_reversed = "%s%s" % (
            x_as_str_reversed[-1],
            x_as_str_reversed[0:-1],
        )

    x_as_int_reversed = int(x_as_str_reversed)

    return check_overflow(x_as_int_reversed)


def main():
    assert reverse_integer(-123) == -321
    assert reverse_integer(321) == 123
    assert reverse_integer(10) == 1
    assert reverse_integer(0) == 0
    assert reverse_integer(1534236469) == 0


if "__main__" == __name__:
    main()
