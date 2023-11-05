class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next is not None:
                curr_node = curr_node.next
            curr_node.next = new_node

    def get(self, index):
        if index < 0:
            return None

        curr_node = self.head
        for i in range(index):
            if curr_node is None:
                return None
            curr_node = curr_node.next

        if curr_node is None:
            return  "Некорректный индекс"

        return curr_node.data

    def remove(self, index):
        if index < 0 or self.head is None:
            return

        if index == 0:
            self.head = self.head.next
            return

        curr_node = self.head
        prev_node = None
        for i in range(index):
            if curr_node is None:
                return
            prev_node = curr_node
            curr_node = curr_node.next

        if curr_node is None:
            return "Некорректный индекс"

        prev_node.next = curr_node.next

    def insert(self, n, val):
        if n < 0:
            return

        new_node = Node(val)
        if n == 0:
            new_node.next = self.head
            self.head = new_node
            return

        curr_node = self.head
        prev_node = None
        for i in range(n):
            if curr_node is None:
                return
            prev_node = curr_node
            curr_node = curr_node.next

        new_node.next = curr_node
        prev_node.next = new_node

    def __iter__(self):
        curr_node = self.head
        while curr_node is not None:
            yield curr_node.data
            curr_node = curr_node.next

linked_list = LinkedList()

linked_list.push(1)
linked_list.push(2)
linked_list.push(3)

for item in linked_list:
    print(item, end=' ')  # Выводит 1, 2, 3

print()
print(linked_list.get(1))  # Выводит 2

linked_list.remove(1)

for item in linked_list:
    print(item, end=' ')  # Выводит 1, 3

print()
linked_list.insert(1, 2)

for item in linked_list:
    print(item, end=' ')  # Выводит 1, 2, 3
