# Status
#   solved by myself        : yes
#   submitted to leetcode   : yes


def halves_are_alike(s: str) -> bool:
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    half_index = len(s) // 2
    vcnt_left, vcnt_right = 0, 0

    if len(s) % 2 != 0:
        return -1

    for item in s[:half_index]:
        if item in vowels:
            vcnt_left += 1

    for item in s[half_index:]:
        if item in vowels:
            vcnt_right += 1

    if vcnt_left == vcnt_right:
        return True
    else:
        return False


assert halves_are_alike("book") is True
assert halves_are_alike("boOM") is True

assert halves_are_alike("hell") is False
assert halves_are_alike("bamboo") is False

assert halves_are_alike("crack") == -1
