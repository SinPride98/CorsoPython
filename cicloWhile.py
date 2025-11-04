
# Scrivi un programma in Python che chieda all’utente di inserire dei numeri interi positivi uno alla volta.

# Il programma deve continuare a chiedere numeri finché la somma totale dei numeri inseriti non supera 100.

# Alla fine, il programma deve stampare:

# 1) La somma totale dei numeri inseriti

# 2) Quanti numeri sono stati inseriti

somma=0
count=0
while somma<100:
    valore=int(input("Inserisci valore:"))
    somma+=valore
    count+=1

print(f"La somma ddei valori è:{somma}")
print(f"Sono stati inseriti {count} numeri")

