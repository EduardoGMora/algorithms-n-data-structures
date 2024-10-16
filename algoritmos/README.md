# Algoritmos de Ordenamiento

Este directorio contiene implementaciones de varios algoritmos de ordenamiento en Python. Estos algoritmos son útiles para entender cómo funcionan diferentes métodos de ordenamiento y para practicar su implementación con arreglos y otras estructuras de datos.

## Algoritmos Implementados

1. **Bubble Sort** - [bubblesort.py](/bubblesort.py)
2. **Insertion Sort** - [insertionsort.py](/insertionsort.py)
3. **Merge Sort** - [mergeSort.py](/mergeSort.py)
4. **Selection Sort** - [selectionsort.py](/selectionsort.py)

## Descripción de los Algoritmos

### Bubble Sort
El algoritmo Bubble Sort compara elementos adyacentes y los intercambia si están en el orden incorrecto. Este proceso se repite hasta que la lista está ordenada.

### Insertion Sort
El algoritmo Insertion Sort construye la lista ordenada de uno en uno, insertando cada nuevo elemento en su posición correcta.

### Merge Sort
El algoritmo Merge Sort divide la lista en mitades, ordena cada mitad y luego las combina en una lista ordenada.

### Selection Sort
El algoritmo Selection Sort selecciona el elemento más pequeño de la lista y lo intercambia con el primer elemento, luego repite el proceso con el resto de la lista.

## Ejecución de los Algoritmos
Cada archivo contiene un ejemplo de cómo ejecutar el algoritmo con una lista de 20 elementos desordenados y mide el tiempo de ejecución.

```python
    # Ejemplo de ejecución 
    lista = [10, 5, 4, 3, 9, 8, 7, 6, 2, 1, 20, 15, 14, 13, 19, 18, 17, 16, 12, 11]
    inicio = time.time()
    print(bublesort(lista))
    fin = time.time()
    print(f'Tiempo de ejecución: {fin-inicio} segundos'´
```

### Practicando con Otras Estructuras
Además de arreglos, busco practicar estos algoritmos con otras estructuras de datos como listas enlazadas, pilas, colas, etc. Puedes encontrar implementaciones de estas estructuras en el directorio estructuras
