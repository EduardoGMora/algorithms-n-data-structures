import time
def insertion(arr):
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

# hazme una lista de 20 elementos desordenados
lista = [10, 5, 4, 3, 9, 8, 7, 6, 2, 1, 20, 15, 14, 13, 19, 18, 17, 16, 12, 11]

inicio= time.time()
print(insertion(lista))
fin = time.time()
print(f'Tiempo de ejecución: {fin-inicio} segundos')