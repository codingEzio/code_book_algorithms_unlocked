from typing import Dict

roman2int: Dict[str, int] = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


# Credit to https://github.com/algorhythms/LeetCode/
def roman_to_int(roman_num: str) -> int:
    output: int = 0

    idx: int
    val: str
    for idx, val in enumerate(roman_num):
        if idx > 0 and roman2int[val] > roman2int[roman_num[idx - 1]]:
            output -= roman2int[roman_num[idx - 1]]
            output += roman2int[val]
        else:
            output += roman2int[val]

    return output


assert roman_to_int("MVIVI") == 1011
