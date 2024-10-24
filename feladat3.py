def osztalyzatok_darabszama(lista, szam):
    db = 0
    i = 0

    while i < len(lista):
        if lista[i] == szam:
            db += 1
        i += 1
    return db
