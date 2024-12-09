def consecutivesum(n):
    times = 0
    start = 1

    while start * (start - 1) // 2 < n:
        if (n - start * (start - 1) // 2) % start == 0:
            times += 1
        start += 1

    return times

print(consecutivesum(int(input())))