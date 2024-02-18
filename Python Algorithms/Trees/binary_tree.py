# To get this to work you might need the following code to add a new path:
# import sys
# sys.path.append("C:\\insert\\path\\to\\Python Algorithms\\")

from Stacks_and_Queues.stack import Stack  
from Stacks_and_Queues.queue import Queue  

class BinaryNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def display_inorder(self, root):
        if root:
            self.display_inorder(root.left)
            print(root.data, end=" "),
            self.display_inorder(root.right)

    def display_preorder(self, root):
        if root:
            print(root.data, end=" "),
            self.display_preorder(root.left)
            self.display_preorder(root.right)
    
    def display_postorder(self, root):
        if root:
            self.display_postorder(root.left)
            self.display_postorder(root.right)
            print(root.data, end=" "),

    def insert(self, data):  
        if self.data is None:  
            self.data = data  
            return  
        if self.data > data:  
            if self.left is None:  
                self.left = BinaryNode(data)  
            else:  
                self.left.insert(data)  
        elif self.data <= data:  
            if self.right is None:  
                self.right = BinaryNode(data)  
            else:  
                self.right.insert(data)

    def delete(self, data):  
        if self.data is None:  
            return None  
  
        if self.data > data:  
            if self.left:  
                self.left = self.left.delete(data)  
        elif self.data < data:  
            if self.right:  
                self.right = self.right.delete(data)  
        else:  
            if self.left is None:  
                return self.right  
            elif self.right is None:  
                return self.left  
            else:  
                min_val = self.right.find_min()  
                self.data = min_val  
                self.right = self.right.delete(min_val)  
        return self  
  
    def find_min(self):  
        if self.left is None:  
            return self.data  
        return self.left.find_min() 
    
    def depth_first_search(self):  
        stack = Stack()
        if self is None:  
            return  
        stack.push(self) 
        while not stack.is_empty():  
            node = stack.pop()  
            print(node.data, end=" ")  
    
            if node.right:  
                stack.push(node.right)  
            if node.left:  
                stack.push(node.left)  
        print()
    
    def breadth_first_search(self):  
        queue = Queue()
        if self is None:  
            return   
        queue.enqueue(self) 
        while not queue.is_empty():  
            node = queue.dequeue()  
            print(node.data, end=" ")  
    
            if node.left:  
                queue.enqueue(node.left)  
            if node.right:  
                queue.enqueue(node.right) 
        print()


# tree = BinaryNode(5)
# tree.left = BinaryNode(3)
# tree.right = BinaryNode(6)
# tree.left.left = BinaryNode(2)

# tree.breadth_first_search()
# output: 5 3 6 2
# tree.depth_first_search()
# output: 5 3 2 6
