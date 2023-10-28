class Node:
    def __init__(self, data):
        self.data = data
        self.pref = None

class Stack:
    def __init__(self):
        self.head = None

    def pop(self):
        if self.head is None:
            raise IndexError("Stack is empty")
        else:
            popped_data = self.head.data
            self.head = self.head.next
            return popped_data

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print(self):
        if self.head is None:
            print("Stack is empty")
        else:
            current = self.head
            while current:
                print(current.data)
                current = current.next

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

stack.print()  # Вывод: 3, 2, 1

print(stack.pop())  # Вывод: 3

stack.print()  # Вывод: 2, 1