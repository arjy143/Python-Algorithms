class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.size += 1

    def pop(self):
        if not self.is_empty():
            item = self.top.data
            self.top = self.top.next
            self.size -= 1
            return item
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.top.data
        else:
            raise IndexError("Stack is empty")

    def is_empty(self):
        return self.size == 0

    def size(self):
        return self.size
    
    def display(self):
        current_node = self.top
        while current_node is not None:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

# stack = Stack()
# stack.push(1)
# stack.display()
# stack.push(2)
# stack.display()
# stack.pop()
# stack.display()
# stack.push(3)
# stack.display()
# stack.push(4)
# stack.display()

# output:
# 1 
# 2 1
# 1
# 3 1
# 4 3 1