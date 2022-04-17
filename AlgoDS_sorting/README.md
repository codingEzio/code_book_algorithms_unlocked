
### Common Sort Algorithms

- [ ] Selection Sort
- [ ] Bubble Sort
- [ ] Insertion Sort
- [ ] Merge Sort
- [ ] Quick Sort
- [ ] Heap Sort
- [ ] Counting Sort
- [ ] Radix Sort
- [ ] Bucket Sort

### HOWTO - profiling

- `python -m cProfile YOUR_SCRIPT.EXTENSION`

### Terminology on *Programming*

- *procedure*: functions, methods
- *call*: run the procedures(functions/methods)
- *parameter*: supply the func with inputs
- *return*: the value which prodecures passed back to its caller
- *array*: aggregates data of the same type into one entity
  - characteristic: it takes equally long to access any elem of an array
- *slot*: each slot corresponds to an array entry (~=index)

### Terminology on *Algorithms*

- *stable algorithm*
    1. In short, with stable algorithms, you're able to get this:

        ```python
        Alice
        Cooper  # suppose you sort the list by the 1st letter
        Johnny
        Conner  # a stable sort'll retain these two names' position
        ```

    2. For more details, check out [*here*](https://stackoverflow.com/a/1517824/6273859) <small>(on stackoverflow)</small>.
