#menu di scelta con while e if 1 menu dei ruoli dove scegliendo il ruolo ti permette di modificare un livello, con 2
#ti permette di aggiungere un nuovo ruolo, con secondo menu modificare i dipendenti,
#stampa unione dei due 

import os
import csv


def modifica_dipendente():
    list_dipendenti = []
    filepath_dipendenti = r'C:\Users\Michael-PC\Desktop\file\dipenti.csv'
    f=open(filepath_dipendenti, 'a')
    f.close()
    with open(filepath_dipendenti, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            list_dipendenti.append(row)
    scelta = 1
    while scelta != 0:

        scelta = int(input("inserisci 0 per uscire, 1 per modificare il dipendente: "))
        if scelta == 1:
            nomeD=input("inserisci il nome nuovo dipendente: ")
            cognomeD=input("inserisci il cognome nuovo dipendente: ")
            ruolo=input("inserisci il ruolo nuovo dipendente: ")
            livello=input("inserisci il livello nuovo dipendente: ")
            list_dipendenti.append({'nome': nomeD, 'cognome': cognomeD, 'ruolo': ruolo, 'livello': livello})
        
        if scelta==2:
            nomeD=input("inserisci il nome dipendente dda eliminare: ")
            for dip in list_dipendenti:
                if dip['nome']==nomeD:
                    list_dipendenti.remove(dip)
        
        if scelta==3:
            nomeD=input("inserisci il nome dipendente a cui modificare il livello: ")
            for dip in list_dipendenti:
                if dip['nome']==nomeD:
                    nuovo_livello=input("inserisci il nuovo livello: ")
                    dip['livello']=nuovo_livello
        
        if scelta==4:
            for dip in list_dipendenti:
                print(dip)
    
        with open(filepath_dipendenti, 'w', newline='') as file:
                fieldnames = ['nome', 'cognome', 'ruolo', 'livello']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for dip in list_dipendenti:
                    writer.writerow(dip)

           
def modifica_ruolo():
    scelta = 1
    while scelta != 0:

        list_ruoli = []

        scelta = int(input("inserisci 0 per uscire, 1 per inserire un livello: "))
        if scelta == 1:
            filepath_ruoli = ricerca_ruolo()
            with open(filepath_ruoli, 'r') as file: 
                reader = csv.DictReader(file)
                for row in reader:
                    list_ruoli.append(row)
            stipendio = input("inserisci lo stipendio: ")
            ore_lavoro = input("inserisci le ore di lavoro: ")
            livello=len(list_ruoli)

            list_ruoli.append({'livello': livello, 'stipendio': stipendio, 'ore_lavoro': ore_lavoro})

        with open(filepath_ruoli, 'w', newline='') as file:
            fieldnames = ['livello', 'stipendio', 'ore_lavoro']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for ruolo in list_ruoli:
                writer.writerow(ruolo)
    
        

def ricerca_ruolo():
    ruoli=os.listdir(r'C:\Users\Michael-PC\Desktop\file\Ruoli')
    for ruolo in ruoli:
        print(ruoli.index(ruolo)+1,":",ruolo)
    scelta=int(input("inserisci il numero del ruolo che vuoi modificare: "))
    return fr'C:\Users\Michael-PC\Desktop\file\Ruoli\{ruoli[scelta-1]}'

def unione():
    filepath_dipendenti = r'C:\Users\Michael-PC\Desktop\file\dipenti.csv'
    dip_ruolo=""
    list_dipendenti = []

    with open(filepath_dipendenti, 'r') as file:
        reader = csv.DictReader(file) 
        print(reader)
        for row in reader:
            print(list_dipendenti)
            list_dipendenti.append(row)
           
    
    for dip in list_dipendenti:
        print(dip['nome'])
        dip_ruolo = dip['ruolo']
        filepath_ruoli = fr'C:\Users\Michael-PC\Desktop\file\{dip_ruolo}.csv'
        with open(filepath_ruoli, 'r') as file_ruolo:
            reader_ruolo = csv.DictReader(file_ruolo)
            list_livelli = [row for row in reader_ruolo]
        with open(r'C:\Users\Michael-PC\Desktop\file\unione.csv', 'w', newline='') as file_unione:
            fieldnames = ['nome', 'cognome', 'ruolo', 'livello', 'stipendio', 'ore_lavoro']
            writer = csv.DictWriter(file_unione, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'nome': dip['nome'], 'cognome': dip['cognome'], 'ruolo': dip['ruolo'], 'livello': dip['livello'],
                             'stipendio': list_livelli[int(dip['livello'])]['stipendio'],
                             'ore_lavoro': list_livelli[int(dip['livello'])]['ore_lavoro']})



scelta = 1

while scelta != 0:
    scelta = int(input("inserisci 0 per uscire, 1 per modificare dipendente, 2 per modificare ruolo, 3 per unione: "))
    if scelta == 1:
        modifica_dipendente()
    if scelta == 2:
        modifica_ruolo()
    if scelta == 3:
        unione()

