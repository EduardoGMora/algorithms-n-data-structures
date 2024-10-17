class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LL:
    def __init__(self):
        self.head = None
        self.tail = None

    def search(self, value):
        temp = self.head
        while temp is not None:
            if temp.value == value:
                return True
            temp = temp.next
        return False

    def agregartail(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def agregarhead(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def agregarpos(self, value, pos):
        if self.head is None:
            return None
        
        if pos == 0:
            self.agregarhead(value)
        elif pos >= self.contar():
            self.agregartail(value)
        else:
            pre = self.head
            for i in range(pos):
                pre = pre.next
                if pre is None:
                    return None

            aft = pre.next
            new_node = Node(value)
            new_node.next = aft
            pre.next = new_node

    def eliminarhead(self):
        if self.head is None:
            return None

        temp = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

        return temp.value

    def contar(self):
        temp = self.head
        contador = 0
        while temp is not None:
            contador += 1
            temp = temp.next
        return contador
    
    def imprimir(self):
        temp = self.head
        while temp is not None:
            print(f'{temp.value}', end=' -> ')
            temp = temp.next


if __name__ == '__main__':
    ll = LL()
    ll.agregartail(1)
    ll.agregartail(2)
    ll.agregartail(3)
    ll.agregarhead(0)
    ll.agregarhead(-1)
    ll.imprimir()
    print()
    print(ll.search(5))
    ll.agregarpos(4, 20)
    ll.imprimir()
    print(f'\n{ll.contar()} elementos')