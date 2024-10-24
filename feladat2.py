
def otosok(lista):
    otos_szam = 0
    i = 0

    while i < len(lista):
        if lista[i] == 5:
            otos_szam+=1
        i += 1

    return otos_szam