# Algorithms
In this Repository I looking to practice and learn more about the sort and search algorithms. I want to understand how works each one and how or when I can use it.


## Sort Algorithms

1. **Bubble Sort** - [bubblesort.py](/algoritmos/bubblesort.py)
3. **Merge Sort** - [mergeSort.py](/algoritmos/mergeSort.py)
2. **Insertion Sort** - [insertionsort.py](/algoritmos/insertionsort.py)
4. **Selection Sort** - [selectionsort.py](/algoritmos/selectionsort.py)

These Algorithms I implemented with arrays but it is possible to use other kind of data structures as Linked List, queues or stacks.

### Descriptions

#### Bubble Sort
The Bubble Sort algorithm compares an item with the next one and switch it if the first one is greater than the second one. This proccess repeats until the list is sorted.

#### Merge Sort
This algorithm is really useful and efficient for longer list, It works dividing the list in smaller lists and sorted each item, then It merges this lists and sorted again. The merge sort best known as divide and conquer, use the recursive call to compare each list and sorted until the first longer list be sorted.

#### Insertion Sort
The Insertion sort receives a list and makes a sorted list

#### Selection Sort
El algoritmo Selection Sort selecciona el elemento más pequeño de la lista y lo intercambia con el primer elemento, luego repite el proceso con el resto de la lista.

- Ejecución de los Algoritmos
Cada archivo contiene un ejemplo de cómo ejecutar el algoritmo con una lista de 20 elementos desordenados y mide el tiempo de ejecución.

```python
    # Ejemplo de ejecución 
    lista = [10, 5, 4, 3, 9, 8, 7, 6, 2, 1, 20, 15, 14, 13, 19, 18, 17, 16, 12, 11]
    inicio = time.time()
    print(bublesort(lista))
    fin = time.time()
    print(f'Tiempo de ejecución: {fin-inicio} segundos'´)
```

## Search Algorithms

1. **DFS** - [DFS.py](/algoritmos/DFS.py)

This algorithms are usually used for data structures as Binary trees or graphs, are really interesting and I really like the idea to know more about them.


### Descriptions
#### DFS
