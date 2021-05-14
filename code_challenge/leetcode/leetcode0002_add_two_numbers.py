# Status
#   core
#       solved by myself        : yes
#       submitted to leetcode   : yes
#   experiment
#       self-contained (stdlib) : yes
#       runnable locally        : yes


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_nums(l1, l2):
    """
    This is probably the most easy-to-understand solution if you know how the
    recursion (call stack) works, and being very familiar with Python language!
    """
    _ = l1.val + l2.val
    digit, tenth = _ % 10, _ // 10
    answer = ListNode(digit)

    if any((l1.next, l2.next, tenth)):
        l1 = l1.next if l1.next else ListNode(0)
        l2 = l2.next if l2.next else ListNode(0)

        l1.val += tenth

        answer.next = add_two_nums(l1, l2)

    return answer


def main():
    L = ListNode

    def to_list(linked_list):
        _list = []

        while True:
            _list.append(linked_list.val)

            if linked_list.next is None:
                break

            linked_list = linked_list.next

        return _list

    # This format plays very nicely with pythontutor, go check it out!
    test1 = (L(0), L(0))
    test2 = (L(2, L(4, L(3))), L(5, L(6, L(4))))
    test3 = (L(1, L(6, L(4, L(2)))), L(2, L(6, L(0, L(2)))))
    test4 = (L(9, L(9, L(9, L(9, L(9, L(9)))))), L(9, L(9, L(9))))
    assert to_list(add_two_nums(*test1)) == [0]
    assert to_list(add_two_nums(*test2)) == [7, 0, 8]
    assert to_list(add_two_nums(*test3)) == [3, 2, 5, 4]
    assert to_list(add_two_nums(*test4)) == [8, 9, 9, 0, 0, 0, 1]


if "__main__" == __name__:
    main()
