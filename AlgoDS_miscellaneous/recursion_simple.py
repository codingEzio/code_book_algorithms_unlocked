def factorial_recur(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        return -1  # invalid
    else:
        return n * factorial_recur(n - 1)


def digit_sum(n: int) -> int:
    if n == 0:
        return 0
    elif n < 0:
        return -1
    elif n > 0:
        pass

    r = 0
    while n:
        r, n = r + n % 10, n // 10
    return r


if __name__ == "__main__":
    assert factorial_recur(-1) == -1
    assert factorial_recur(0) == 1
    assert factorial_recur(1) == 1
    assert factorial_recur(3) == 6

    assert digit_sum(-123) == -1
    assert digit_sum(0) == 0
    assert digit_sum(1) == 1
    assert digit_sum(123) == 6
