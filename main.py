import feladat1
import feladat2
import feladat3

lista = [5,2,3,4,4,5,5,5,1,2,2,3,4,5,5,5,4,3,3] 


jegyek_atlaga=feladat1.jegyek_atlaga(lista)
print(f"A diákok jegyeinek átlaga: {jegyek_atlaga:.2f}")


otosok = feladat2.otosok(lista)
print(f"Összesen {otosok} ötös van.")


akik_egyest_kaptak = feladat3.egyesek(lista)
print(f"Összesen {akik_egyest_kaptak} en kaptak egyest.")



