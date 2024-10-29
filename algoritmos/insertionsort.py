import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../estructuras')))
import LL

def staticInsertion(arr):
    if arr is None:
        return
    
    for i in range(1, len(arr)):
        key = arr[i]
        j= i -1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


def dynamicInsertion(LL):
    if LL is None:
        return


# hazme una arreglo de 20 elementos desordenados
lista = [10, 5, 4, 3, 9, 8, 7, 6, 2, 1, 20, 15, 14, 13, 19, 18, 17, 16, 12, 11]

inicio= time.time()
print(staticInsertion(lista))
fin = time.time()
print(f'Tiempo de ejecución: {fin-inicio} segundos')