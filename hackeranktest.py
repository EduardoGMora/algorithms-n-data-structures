# Description: This file contains some algorithms and data structures problems from HackerRank

# Obtiene el número de veces que se puede sumar un número consecutivo para obtener un número dado
def consecutivesum(n):
    times = 0
    start = 1

    while start * (start - 1) // 2 < n:
        if (n - start * (start - 1) // 2) % start == 0:
            times += 1
        start += 1

    return times

print(consecutivesum(int(input())))


# Obtiene el número de veces que un jugador gana a los demás en un juego de "mejor de tres"
def mejor_jugador(arr1, arr2, arr3):
    jugadores = [
        [arr1[0], arr2[0], arr3[0]],  # Números del jugador 1
        [arr1[1], arr2[1], arr3[1]],  # Números del jugador 2
        [arr1[2], arr2[2], arr3[2]],  # Números del jugador 3
        [arr1[3], arr2[3], arr3[3]]   # Números del jugador 4
    ]
    n_jugadores = len(jugadores)
    resultados = [0] * n_jugadores  # Lleva la cuenta de a cuántos gana cada jugador

    # Simular enfrentamientos entre todos los jugadores
    for i in range(n_jugadores):
        for j in range(n_jugadores):
            if i != j:
                jugador_a = jugadores[i]
                jugador_b = jugadores[j]

                # Evaluar "mejor de tres"
                rondas_ganadas_a = 0
                rondas_ganadas_b = 0

                for x in range(3):
                    for y in range(3):
                        if jugador_a[x] > jugador_b[y]:
                            rondas_ganadas_a += 1
                        elif jugador_b[y] > jugador_a[x]:
                            rondas_ganadas_b += 1

                if rondas_ganadas_a > rondas_ganadas_b:
                    resultados[i] += 1

    # Determinar el jugador que gana a la mayor cantidad de jugadores
    max_victorias = max(resultados)
    ganador = resultados.index(max_victorias) + 1  # Para indexar jugadores desde 1

    return ganador, resultados

# Ejemplo de uso
arr1 = [3, 7, 5, 8]
arr2 = [2, 9, 4, 6]
arr3 = [1, 6, 8, 7]

mejor, resultados = mejor_jugador(arr1, arr2, arr3)
print(f"El jugador que gana a la mayor cantidad de jugadores es el Jugador {mejor}.")
print(f"Resultados: {resultados}")

