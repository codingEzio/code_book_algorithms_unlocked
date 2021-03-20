# Status
#   solved by myself        : no
#   submitted to leetcode   : no
from typing import List, Union


# Credit to 'https://stackoverflow.com/a/53526895/6273859' for returning type
def fizzbuzz(n: int, fizz=3, buzz=5) -> List[Union[str, int]]:
    if n < 1:
        raise ValueError("n cannot be less than 1")
    if n is None:
        raise TypeError("n cannot be None")

    result: List[Union[str, int]] = []

    i: int
    for i in range(1, n + 1):
        if i % fizz == 0 and i % buzz == 0:
            result.append("FizzBuzz")
        elif i % fizz == 0:
            result.append("Fizz")
        elif i % buzz == 0:
            result.append("Buzz")
        else:
            result.append(i)

    return result
