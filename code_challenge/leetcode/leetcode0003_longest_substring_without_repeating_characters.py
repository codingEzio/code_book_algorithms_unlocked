# Status
#   core
#       solved by myself        : yes
#       submitted to leetcode   : yes
#   experiment
#       self-contained (stdlib) : yes
#       runnable locally        : yes


def length_of_longest_substring(s: str) -> int:
    len_longest_substr = 0
    current_substr = ""

    for current_single_char in s:
        if (current_single_char in current_substr) is False:
            current_substr += current_single_char
        else:
            len_longest_substr = (
                len_longest_substr
                if len_longest_substr > len(current_substr)
                else len(current_substr)
            )
            current_substr = (
                current_substr[current_substr.index(current_single_char) + 1 :]
                + current_single_char
            )

    len_longest_substr = (
        len_longest_substr
        if len_longest_substr > len(current_substr)
        else len(current_substr)
    )

    return len_longest_substr


def main():
    assert length_of_longest_substring("pwwkew") == 3
    assert length_of_longest_substring("aaaaa") == 1
    assert length_of_longest_substring("") == 0


if "__main__" == __name__:
    main()
