from random import choices
from annotated_types import IntList


def randomize(arr: IntList):
    length: int = len(arr)
    return choices(arr, k=length)


def sort_inputs(func, arr: IntList):
    return func(arr)
