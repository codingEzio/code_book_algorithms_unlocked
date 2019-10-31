
from annotated_types import IntList
from utils import randomize


def quick_sort(arr: IntList) -> IntList:
    less: IntList = []
    pivotList: IntList = []
    more: IntList = []

    if len(arr) <= 1:
        print(f"[in len(arr)] 🧐 {arr}")
        return arr
    else:
        pivot: int = arr[len(arr) // 2]
        # pivot: int = arr[0]
        for i in arr:
            print('\n[Start iteration 🍰]')
            if i < pivot:
                less.append(i)
                print(f'[in loop LESS] 1️⃣ {less} 2️⃣ {more} 3️⃣ {pivotList}')
            elif i > pivot:
                more.append(i)
                print(f'[in loop MORE] 1️⃣ {less} 2️⃣ {more} 3️⃣ {pivotList}')
            else:
                pivotList.append(i)
                print(f'[in loop PIVO] 1️⃣ {less} 2️⃣ {more} 3️⃣ {pivotList}')

        less = quick_sort(less)
        more = quick_sort(more)
        return less + pivotList + more


if __name__ == "__main__":
    inputs: IntList = [6, 9, 7, 8, 4, 5, 10]
    sorted_inputs: IntList = [4, 5, 6, 7, 8, 9, 10]

    randomize(inputs)
    assert quick_sort(inputs) == sorted_inputs
