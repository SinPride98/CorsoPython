#inventario proddotto{quantita,prezzo unitario,nome prodotto} tramite selezione ricercare:
#prezzo e quantita in base all nome del prodotto,agggiungegr un prodotto,ricaricare la quantita in base al nome
#modifica prezzo in base al nome

scelta=1
list=[{'nome':"colla",'quantita':10,'prezzo':5.50}]

while scelta!=0:
    scelta=int(input("inserisci scelta:"))
    
    if scelta==1:
        nomeP=input("Inserisci nome:")
        q=int(input("inserisci quantita:"))
        prezzo=float(input("inserisci prezzo:"))
        list.append({'nome':nomeP,'quantita':q,'prezzo':prezzo})
    
    elif scelta==2:
        nomeP=input("Inserisci nome prodotto da cercare:")
        for prodotto in list:
            if prodotto['nome']==nomeP:
                print(str(prodotto['prezzo'])+" ",prodotto['quantita'])
    
    elif scelta==3:
        nomeP=input("Inserisci nome prodotto da cercare:")
        for prodotto in list:
            if prodotto['nome']==nomeP:
               q=int(input("inserisci nuova quantita:"))
               prodotto['quantita']+=q
        print(list)
    
    elif scelta==4:
        nomeP=input("Inserisci nome prodotto da cercare:")
        for prodotto in list:
            if prodotto['nome']==nomeP:
               prezzo=float(input("inserisci nuova quantita:"))
               prodotto['prezzo']=prezzo
        print(list)
    
    elif scelta==5:
        totP=0
        for prodotto in list:
            totP=totP+prodotto['prezzo']*prodotto['quantita']
        print(totP)
    
    elif scelta==6:
        noIva=0
        nomeP=input("Inserisci nome prodotto da cercare:")
        for prodotto in list:
            if prodotto['nome']==nomeP:
                noIva=prodotto['prezzo']-prodotto['prezzo']*0.22
                print("iva:",prodotto['prezzo']*0.22,"  prezzo senza iva:" ,noIva)
    
 
