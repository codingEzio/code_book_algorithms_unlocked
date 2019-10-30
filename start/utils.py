from random import choices
from annotated_types import IntList


def randomize(arr: IntList):
    length: int = len(arr)
    return choices(arr, k=length)


def sort_inplace(func, arr: IntList):
    return func(arr)
