class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def peekfront(self):
        if self.head is None:
            return None
        return self.head.value
    
    def peekback(self):
        if self.tail is None:
            return None
        return self.tail.value

    def enqueue(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def dequeue(self):
        if self.head is None:
            return None
        
        temp = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        
        return temp.value
    
if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.dequeue()
    print(queue.peekfront())
    print(queue.peekback())
    queue.enqueue(4)
    queue.enqueue(5)
    print(queue.peekfront())
    print(queue.peekback())