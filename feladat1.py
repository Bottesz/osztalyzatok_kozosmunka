
def jegyek_atlaga(lista):
    osszeg:int=0
    i:int=0
    atlag:int=0
    while i<len(lista):
        osszeg+=lista[i]
        i+=1
    atlag = osszeg/len(lista)
    return atlag


