class Node:
    def __init__(self, value):
        self.value: int = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node: Node = Node(value)
        self.head = new_node
        self.tail = new_node
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
            new_node.prev: Node = self.tail
            self.tail: Node = new_node
            self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp: Node = self.tail
        if self.length == 1:
            self.head: Node = None
            self.tail: Node = None
        else:
            self.tail: Node = self.tail.prev
            self.tail.next: Node = None
            temp.prev: Node = None
            self.length -= 1
        return temp

    def prepend(self, value):
        new_node: Node = Node(value)
        if self.head is None:
            self.head: Node = new_node
            self.tail: Node = new_node
            self.length: int = 1
        else:
            new_node.next: Node = self.head
            self.head.prev: Node = new_node
            self.head: Node = new_node
            self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp: Node = self.head
        if self.length == 1:
            self.head: Node = None
            self.tail: Node = None
        else:
            self.head: Node = self.head.next
            self.head.prev: Node = None
            temp.next: Node = None
            self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp: Node = self.head
        if index < self.length / 2:
            for _ in range(index):
                temp: Node = temp.next
        else:
            temp: Node = self.tail
            for _ in range(self.length - 1, index, -1):
                temp: Node = temp.prev
        return temp

    def set_value(self, index, value):
        temp: Node = self.get(index)
        if temp:
            temp.value: int = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node: Node = Node(value)
        temp: Node = self.get(index - 1)
        new_node.next: Node = temp.next
        temp.next.prev: Node = new_node
        temp.next: Node = new_node
        new_node.prev: Node = temp
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temp: Node = self.get(index)
        temp.prev.next: Node = temp.next
        temp.next.prev: Node = temp.prev
        temp.next: Node = None
        temp.prev: Node = None
        self.length -= 1
        return temp
