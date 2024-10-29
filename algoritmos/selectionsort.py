import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../estructuras')))
import LL

def SelectionSortArr(arr):
    if arr is None:
        return

    for i in range(len(arr)):
        minimo = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minimo]:
                minimo = j
            arr[i], arr[minimo] = arr[minimo], arr[i]
    return arr
        
def SelectionSortLL(LL):
    if LL is None:
        return
    
    current = LL.head
    for current in range(LL.contar()):
        minimo = current
        for i in range (current.next,LL.contar()):
            if i.value < current.value:
                minimo = i
            current.value, minimo.value = minimo.value, current.value
    return LL

# hazme una lista de 20 elementos desordenados
arreglo = [10, 5, 4, 3, 9, 8, 7, 6, 2, 1, 20, 15, 14, 13, 19, 18, 17, 16, 12, 11]

# crear una lista ligada con los mismos elementos
linkedlist = estructuras.LL.LL()
for i in arreglo:
    linkedlist.agregartail(i)


inicio = time.time()
print(SelectionSortArr(arreglo))
SelectionSortLL(linkedlist).imprimir()
fin = time.time()