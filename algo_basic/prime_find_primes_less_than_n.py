"""
This is an implementation based the ancient algorithm for finding
all prime numbers up to any given limit (aka. Sieve of Eratosthenes).
"""
from utils.annotated_types import IntList, BoolList


def get_primes(n: int) -> IntList:
    """Return list of all primes less than n,
    Using sieve of Eratosthenes.
    """
    if n <= 0:
        raise ValueError("'n' must be a positive integer.")

    sieve_size: int
    if n % 2 == 0:
        sieve_size = n // 2 - 1
    else:
        sieve_size = n // 2

    sieve: BoolList = [True for _ in range(sieve_size)]
    prime_list: IntList = []
    if n >= 2:
        prime_list.append(2)

    for i in range(sieve_size):
        if sieve[i]:
            value_at_i = i * 2 + 3
            prime_list.append(value_at_i)

            for j in range(i, sieve_size, value_at_i):
                # print(i, sieve[i])
                # print(j, sieve_size, value_at_i)
                sieve[j] = False

    return prime_list


if __name__ == "__main__":
    inputs: IntList = [17, 25, 1000]
    for i in inputs:
        print(f"{i:>2} {get_primes(i)}")
