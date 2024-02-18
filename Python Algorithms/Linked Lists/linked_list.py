class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
    
    def insert(self, data, index):
        if index < 0:
            return
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current_node = self.head
            count = 0
            while count < index - 1 and current_node.next is not None:
                current_node = current_node.next
                count += 1
            new_node.next = current_node.next
            current_node.next = new_node

    def delete(self, data):
        current_node = self.head
        previous_node = None
        while current_node is not None:
            if current_node.data == data:
                if previous_node is None:
                    self.head = current_node.next
                else:
                    previous_node.next = current_node.next
                return

            previous_node = current_node
            current_node = current_node.next

    def reverse(self):
        reversed_list = LinkedList()
        current_node = self.head
        while current_node is not None:
            reversed_list.insert(current_node.data, 0)
            current_node = current_node.next
        return reversed_list

    def display(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

# my_list = LinkedList()
# my_list.append(1)
# my_list.append(3)
# my_list.append(4)
# my_list.insert(2,1)
# my_list.delete(3)
# reversed_list = my_list.reverse()
# my_list.display()  # Output: 1 2 4
# reversed_list.display() # output: 4 2 1
