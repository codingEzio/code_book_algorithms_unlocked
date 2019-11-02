### HOWTO - profiling

- `python -m cProfile YOUR_SCRIPT.EXTENSION`

### Terminology on *Programming*

- _procedure_: functions, methods
- _call_: run the procedures(functions/methods)
- _parameter_: supply the func with inputs
- _return_: the value which prodecures passed back to its caller
- _array_: aggregates data of the same type into one entity
  - characteristic: it takes equally long to access any elem of an array
- _slot_: each slot corresponds to an array entry (~=index)

### Terminology on *Algorithms*

- _stable algorithm_
    1. In short, with stable algorithms, you're able to get this:
        ```python
        Alice
        Cooper  # suppose you sort the list by the 1st letter
        Johnny
        Conner  # a stable sort'll retain these two names' position
        ```
    2. For more details, check out [*here*](https://stackoverflow.com/a/1517824/6273859) <small>(on stackoverflow)</small>.
