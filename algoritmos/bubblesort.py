import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../estructuras')))
import LL

def bublesort(arr):
    if arr is None:
        return

    size = len(arr)
    for i in range(0, size):
        for j in range (0, size - 1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

# Un arreglo de 20 elementos desordenados
arreglo = [10, 5, 4, 3, 9, 8, 7, 6, 2, 1, 20, 15, 14, 13, 19, 18, 17, 16, 12, 11]

linkedlist = estructuras.LL.LL()
for i in arreglo:
    linkedlist.agregartail(i)

inicio= time.time()
print(bublesort(lista))
fin = time.time()
print(f'Tiempo de ejecución: {fin-inicio} segundos')