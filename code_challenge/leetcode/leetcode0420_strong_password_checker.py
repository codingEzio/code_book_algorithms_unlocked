# Status
#   core
#       solved by myself        : not yet
#       submitted to leetcode   : not yet
#   experiment
#       self-contained (stdlib) : yes
#       runnable locally        : yes
from collections import Counter


def strong_password_checker(password: str) -> int:
    """
    Given a password, return the minimum steps required to make password strong
    >>> "a"         # 5
    >>> "aA1"       # 3
    >>> "1337x029"  # 0

    What counts as "strong" here
    0. possible string occurence: a-z A-Z . !
    1. min: 6, max: 20
    2. no three-repeating characters (no: 111a, 2!!!)
    3. at least one uppercase, one lowercase, one digit

    About the symbols ('.' and '!')
    1. don't worry about it, you do NOT need to handle them
    2. the three-repeating rule still applies (!!!1 -> weak)

    About the "step" (either opt count as one)
    1. <insert>  ONE character to password
    2. <delete>  ONE character to password
    3. <replace> ONE character with another character
    """
    # As long as it isn't "too short" or "too long", we could still try to
    # transform the password into a stronger one (problem constraints).
    if 0 >= len(password) and len(password) > 50:
        return None

    string_occurence = Counter(password)

    if len(password) == 1:
        return 5
    elif len(password) == 2:
        return 4
    else:
        pass


def main():
    assert strong_password_checker("a") == 5
    # assert strong_password_checker("aA1") == 3
    # assert strong_password_checker("1337x619") == 0


if "__main__" == __name__:
    main()
