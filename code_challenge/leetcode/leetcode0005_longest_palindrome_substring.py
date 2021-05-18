# Status
#   core
#       solved by myself        : yes
#       submitted to leetcode   : yes
#   experiment
#       self-contained (stdlib) : yes
#       runnable locally        : yes


def longest_palindrome_substring(s: str) -> str:
    def max_palindrome(s, expandfrommid_left, expandfrommid_right, result):
        substr = ""

        while (
            expandfrommid_left >= 0
            and expandfrommid_right < len(s)
            and s[expandfrommid_left] == s[expandfrommid_right]
        ):
            substr = s[expandfrommid_left : expandfrommid_right + 1]
            expandfrommid_left -= 1
            expandfrommid_right += 1

        if len(result) < len(substr):
            return substr

        return result

    result = ""
    for i in range(len(s)):
        result = max_palindrome(s, i, i, result)
        result = max_palindrome(s, i, i + 1, result)

    return result


def main():
    assert longest_palindrome_substring("babadd") == "aba" or "bab"
    assert longest_palindrome_substring("bcace") == "cac"
    assert longest_palindrome_substring("cbbd") == "bb"
    assert longest_palindrome_substring("ac") == "c" or "a"
    assert longest_palindrome_substring("a") == "a"
    assert longest_palindrome_substring("") == ""


if "__main__" == __name__:
    main()
