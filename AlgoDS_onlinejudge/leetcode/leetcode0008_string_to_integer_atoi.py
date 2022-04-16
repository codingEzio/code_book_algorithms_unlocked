# Status
#   core
#       solved by myself        : yes
#       submitted to leetcode   : yes
#   experiment
#       self-contained (stdlib) : yes
#       runnable locally        : yes


def string_to_integer_atoi(s):
    limits = {"max": +(2 ** 31) - 1, "min": -(2 ** 31)}

    s = s.strip()

    if len(s) == 0:
        return 0

    positive_or_not = 1
    if s[0] in ["+", "-"]:
        if s[0] == "-":
            positive_or_not = -1

        s = s[1:]

    answer = 0
    for single_char in s:
        if single_char.isdigit():
            answer = answer * 10 + int(single_char)
        else:
            break

    answer *= positive_or_not

    if answer >= limits["max"]:
        return limits["max"]
    if answer <= limits["min"]:
        return limits["min"]

    return answer


def main():
    assert string_to_integer_atoi("42") == 42
    assert string_to_integer_atoi("    -42") == -42
    assert string_to_integer_atoi("9846 in sqaure") == 9846
    assert string_to_integer_atoi("square in 9846") == 0
    assert string_to_integer_atoi("-55555666666") == -2147483648


if "__main__" == __name__:
    main()
