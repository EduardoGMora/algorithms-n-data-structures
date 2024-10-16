import time

def bublesort(arr):
    if arr is None:
        return

    size = len(arr)
    for n in range(0,size):
        for i in range(0,size-n-1): 
            siguiente = i+1
            if arr[i] > arr[siguiente]:
                arr[i], arr[siguiente] = arr[siguiente], arr[i]
            i += 1
        n += 1
    return arr

# hazme una lista de 20 elementos desordenados
lista = [10, 5, 4, 3, 9, 8, 7, 6, 2, 1, 20, 15, 14, 13, 19, 18, 17, 16, 12, 11]
inicio= time.time()
print(bublesort(lista))
fin = time.time()
print(f'Tiempo de ejecución: {fin-inicio} segundos')