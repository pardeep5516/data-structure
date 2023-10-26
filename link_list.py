class Node:
    def __init__(self, value):
        self.value: int = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node: Node = Node(value)
        self.head: Node = new_node
        self.tail: Node = new_node
        self.length: int = 1

    def print_list(self) -> list:
        temp: Node = self.head
        all_node: list = []
        while temp is not None:
            all_node.append(temp.value)
            temp: Node = temp.next
        return all_node

    def link_list_length(self) -> int:
        return self.length

    def append(self, value) -> bool:
        new_node: Node = Node(value)
        if self.head is None:
            self.head: Node = new_node
            self.tail: Node = new_node
            self.length: int = 1
        else:
            self.tail.next: Node = new_node
            self.tail: Node = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp: Node = self.head
        pre: Node = self.head
        while temp.next is not None:
            pre: Node = temp
            temp: Node = temp.next
        self.tail: Node = pre
        self.tail.next: Node = None
        self.length -= 1
        if self.length == 0:
            self.head: Node = None
            self.tail = None
        return temp

    def prepend(self, value) -> bool:
        new_node: Node = Node(value)
        if self.head is None:
            self.head: Node = new_node
            self.tail: Node = new_node
            self.length: int = 1
        else:
            new_node.next: Node = self.head
            self.head: Node = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp: Node = self.head
        self.head: Node = self.head.next
        temp.next: Node = None
        self.length -= 1
        if self.length == 0:
            self.tail: Node = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp: Node = self.head
        for _ in range(index):
            temp: Node = temp.next
        return temp

    def set_value(self, index, value) -> bool:
        temp: Node = self.get(index)
        if temp:
            temp.value: Node = value
            return True
        return False

    def insert(self, index, value) -> bool:
        if index < 0 or index > self.length:
            return False
        if index == 0:
            self.prepend(value)
            return True
        if index == self.length:
            self.append(value)
            return True
        new_node: Node = Node(value)
        temp: Node = self.get(index - 1)
        new_node.next: Node = temp.next
        temp.next: Node = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre: int = self.get(index - 1)
        temp: Node = pre.next
        pre.next: Node = temp.next
        temp.next: Node = None
        self.length -= 1
        return temp

    def reverse(self):
        if self.length == 0:
            return None
        if self.length == 1:
            return self.head
        temp: Node = self.head
        self.head: Node = self.tail
        self.tail: Node = temp
        after: Node = temp.next
        before = None
        for _ in range(self.length):
            after: Node = temp.next
            temp.next: Node = before
            before: Node = temp
            temp: Node = after
        return True
