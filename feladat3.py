def egyesek(lista):
    akikkaptak = 0
    i = 0

    while i < len(lista):
        if lista[i] <=2:
            akikkaptak += 1
        i += 1
    return akikkaptak
