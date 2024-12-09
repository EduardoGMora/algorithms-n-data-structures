class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Grafo:
    def __init__(self):
        self.vertices = {}
        self.edges = {}
