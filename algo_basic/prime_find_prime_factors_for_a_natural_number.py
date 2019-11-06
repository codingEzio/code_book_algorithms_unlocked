from utils.annotated_types import IntList


def trial_division(n: int) -> IntList:
    """
    Given an number 12, it should return prime factors [2, 2, 3].

    Related links:
    ~ https://en.wikipedia.org/wiki/Trial_division
    ~ https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    """

    prime_list: IntList = []
    while n % 2 == 0:
        prime_list.append(2)
        n = n // 2

    f: int = 3
    while f ** 2 <= n:
        if n % f == 0:
            prime_list.append(f)
            n = n // f
        else:
            f = f + 2

    if n != 1:
        prime_list.append(n)

    return prime_list


if __name__ == "__main__":
    inputs: IntList = [4, 5, 13, 15]
    for i in inputs:
        print(f"{i:>2} {trial_division(i)}")
