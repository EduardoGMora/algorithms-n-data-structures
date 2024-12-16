import time
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../estructuras')))
import grafos as g

def DFS(graph, start, visited=None):
    try: 
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=' ')
        for neighbor, _ in graph.vertexList[start].neighbors:
            if neighbor.value not in visited:
                DFS(graph, neighbor.value, visited)
    except KeyError:
        print('No existe el nodo', start)
        return


if __name__ == '__main__':
    #grafo no dirigido
    grafo1 = g.Graph()
    grafo1.add_vertex('A')
    grafo1.add_vertex('B')
    grafo1.add_vertex('C')
    grafo1.add_vertex('D')
    grafo1.add_edge('A', 'B', 5)
    grafo1.add_edge('A', 'C', 3)
    grafo1.add_edge('A', 'D', 2)
    grafo1.add_edge('B', 'C', 1)
    grafo1.add_edge('B', 'D', 4)
    grafo1.add_edge('C', 'D', 6)
    grafo1.display()

    print('DFS:')
    DFS(grafo1, 'g')
