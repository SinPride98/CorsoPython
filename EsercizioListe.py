# Calcola la somma totale dei numeri all'interno della lista seguente: 

"""lista = [[1,2,3], [4,5]]
somma=0
for liste in lista:
    for valore in liste:
        somma+=valore"""


#Scrivi una funzione func che date due liste restituisce una lista che contiene gli elementi a comune tra due liste e fai un esempio

def func(lst1,lst2):
    lista=[]
    for l1 in lst1:
        for l2 in lst2:
            if l1==l2:
                lista.append(l1)
    return lista

lista1=[1,2,3,4,5]
lista2=[2,4,6,8]

print(f"lista numeri in comune:{func(lista1,lista2)}")

