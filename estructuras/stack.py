class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
    
    def peek(self):
        if self.head is None:
            return None
        return self.head.value
    
    def pop(self):
        if self.head is None:
            return None
        temp = self.head
        self.head = self.head.next
        return temp.value
    

if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.pop()
    stack.push(4)
    stack.push(5)
    stack.push(6)
    stack.push(7)
    stack.pop()
    stack.push(8)
    stack.push(9)
    stack.push(10)
    print(stack.pop())
    print(stack.peek())