from random import shuffle
from annotated_types import IntList, Function


def randomize(arr: IntList) -> None:
    """Randomize an array/list in place.
    Reference: https://stackoverflow.com/a/976921
    """
    return shuffle(arr)


def sort_inplace(func: Function, arr: IntList):
    """Sort an array/list in place
    """
    return func(arr)
