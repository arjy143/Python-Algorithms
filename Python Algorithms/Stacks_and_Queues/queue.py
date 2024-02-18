class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.bottom = None
        self.top = None
        self.queue_size = 0

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.top = new_node
            self.bottom = new_node
        else:
            self.top.next = new_node
            self.top = new_node
        self.queue_size += 1

    def dequeue(self):
        if not self.is_empty():
            item = self.bottom.data
            if self.queue_size == 1:
                self.bottom = None
                self.top = None
            else:
                self.bottom = self.bottom.next
            self.queue_size -= 1
            return item
        else:
            raise IndexError("Queue is empty")

    def peek(self):
        if not self.is_empty():
            return self.bottom.data
        else:
            raise IndexError("Queue is empty")

    def is_empty(self):
        return self.queue_size == 0

    def size(self):
        return self.queue_size

    def display(self):
        current_node = self.bottom
        while current_node is not None:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()


# queue = Queue()
# queue.enqueue(1)
# queue.display()
# queue.enqueue(2)
# queue.display()
# queue.dequeue()
# queue.display()
# queue.enqueue(3)
# queue.display()
# queue.enqueue(4)
# queue.display()
# queue.dequeue()
# queue.display()

# output: 
# 1 
# 1 2
# 2
# 2 3
# 2 3 4
# 3 4