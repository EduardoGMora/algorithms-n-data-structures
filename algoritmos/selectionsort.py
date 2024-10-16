import time

def selection(arr):
    for i in range(len(arr)):
        minimo = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minimo]:
                minimo = j
            arr[i], arr[minimo]= arr[minimo], arr[i]
    return arr

# hazme una lista de 20 elementos desordenados
lista = [10, 5, 4, 3, 9, 8, 7, 6, 2, 1, 20, 15, 14, 13, 19, 18, 17, 16, 12, 11]
inicio = time.time()
print(selection(lista))
fin = time.time()