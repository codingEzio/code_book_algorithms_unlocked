def is_prime(n: int) -> bool:
    if n <= 1 or n == 0:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    # test all candidate divisors from 2 through n − 1
    for item in range(3, int(n / 2) + 1, 2):
        if n % item == 0:
            return False

    return True


def is_prime_another_impl(n: int) -> bool:
    if n <= 1:
        return False
    elif n == 2 or n == 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return True
        i += 6

    return True


if __name__ == "__main__":
    pass
