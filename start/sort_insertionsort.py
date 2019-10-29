from annotated_types import IntList


def insertion_sort(arr: IntList):
    for idx in range(1, len(arr)):
        current_val = arr[idx]
        i = idx - 1
        while i >= 0 and current_val < arr[i]:
            arr[i+1] = arr[i]
            arr[i] = current_val
            i = i - 1
    return arr


if __name__ == "__main__":
    inputs: IntList = [6, 7, 8, 3, 4, 5]
    sorted_inputs: IntList = insertion_sort([6, 7, 8, 3, 4, 5])
    assert insertion_sort(inputs) == sorted_inputs
