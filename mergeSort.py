import time

def mergeSort(arr) :

    if arr is None:
        return

    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1

            k += 1

         # Copiar los elementos restantes de L, si los hay
        for i in range(i, len(L)):
            arr[k] = L[i]
            i += 1
            k += 1

        # Copiar los elementos restantes de R, si los hay
        for j in range(j, len(R)):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr

# hazme una lista de 20 elementos desordenados
lista = [10, 5, 4, 3, 9, 8, 7, 6, 2, 1, 20, 15, 14, 13, 19, 18, 17, 16, 12, 11]
inicio= time.time()
print(mergeSort(lista))
fin = time.time()
print(f'Tiempo de ejecución: {fin-inicio} segundos')