
lista = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
scores = {}
for student in lista:
        name, score = student
        if score in scores:
            scores[score].append(name)
        else:
            scores[score] = [name]
                
duplicados = {scr: nombres for scr, nombres in scores.items() if len(nombres) > 1}

for score in duplicados:
    for name in sorted(duplicados[score]):
        print(name)