class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def pop(self):
        if self.head is None:
            raise IndexError("Queue is empty")

        data = self.head.data
        if self.head.next is not None:
            self.head.next.prev = None
        self.head = self.head.next
        if self.head is None:
            self.tail = None

        return data

    def push(self, data):
        new_node = Node(data)
        if self.tail is not None:
            self.tail.next = new_node
            new_node.prev = self.tail
        if self.head is None:
            self.head = new_node
        self.tail = new_node

    def insert(self, n, val):
        if n <= 0:
            self.push(val)
            return

        new_node = Node(val)
        current = self.head
        count = 1
        while current is not None and count < n:
            current = current.next
            count += 1

        if current is None:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            new_node.prev = current.prev
            new_node.next = current
            current.prev.next = new_node
            current.prev = new_node

    def print(self):
        current = self.head
        result = []
        while current is not None:
            result.append(current.data)
            current = current.next
        print(result)


queue = Queue()
queue.push(1)
queue.push(2)
queue.push(3)

queue.print() #Выведет список состоящий из 1,2 и 3

queue.insert(2, 5) #Добавит 5ку по индексу n-1
queue.insert(4, 4) #Добавит 4ку по индексу n-1
queue.print()

queue.pop() #удалит 0й элемент из списка 4 чисел
queue.pop() #удалит 0й элемент из списка 3 чисел

queue.print()