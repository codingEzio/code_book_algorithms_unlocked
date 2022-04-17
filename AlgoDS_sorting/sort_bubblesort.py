# References
# https://stackabuse.com/bubble-sort-in-python/


def bubble_sort(arr, debug=False):
    """
    Bubble sort is one of most worst-performing sorting algorithms.
    The comparison is bubbling up the array items as its name suggests.

    Take [3, 9, 1, 5] as an example
    - 3, 9, 1, 5  { loop1, initial }
    - 3, 1, 9, 5  { loop1, 3<1 fine => 9<1 not fine }
    - 3, 1, 5, 9  { loop1, 3<1 fine => 1<9 fine, 9<5 not fine }
    - 1, 3, 5, 9  { loop2, 3<1 not fine => the end }
    """
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                if debug:
                    print(f"INFO {arr}")


def bubble_sort_improved(arr):
    has_swaped = True

    while has_swaped:
        has_swaped = False

        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

                has_swaped = True
