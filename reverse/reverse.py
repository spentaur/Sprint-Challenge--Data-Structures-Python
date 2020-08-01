class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return str(self.value)

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # not too big a fan of this solution, not sure if it's the best way to
        # do it, i could probably do recursion, but it works, and passes the
        # tests.
        if node is None:
            return

        while node.get_next():
            next_node = node.get_next()
            node.set_next(prev)
            prev = node
            node = next_node

        node.set_next(prev)
        self.head = node
