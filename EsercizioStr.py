"""Scrivi una funzione func che riceve due parametri:

- una lista di stringhe

- una lettera

la funzione deve restituire una lista contenente solo quelle stringhe che contengono la lettera"""


def func(listaStr,lettera):
    listaLetStr=[]
    for stringa in listaStr:
        if lettera in stringa:
            listaLetStr.append(stringa.count(lettera))
    return listaLetStr
    
lista=["ciao","casa","chiosco","canarino"]
let=input("inserisci una lettera:")
print(f"lista di parole con lettera in comune:{func(lista,let)}")