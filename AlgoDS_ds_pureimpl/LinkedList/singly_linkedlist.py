class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def remove(self, item):
        current = self.head
        found = False
        previous = None

        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self.head = current.get_next()
        elif previous is not None and current is not None:
            previous.set_next(current.get_next())
        else:
            print("The item does not exist")
