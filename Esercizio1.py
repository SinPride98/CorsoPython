
list=[]
list.append({'nome':"michael",'cognome':"ranieri",'numtel':"3333333"})
print(list)
scelta=1
while scelta!=0:
    scelta=int(input("inserisci scelta:"))
    if scelta==1:
        nome=input("inserisci nome:")
        cognome=input("inserisci cognome:")
        numtel=input("inserisci numero di telefono:")
        list.append({'nome':nome,'cognome':cognome,'numtel':numtel})
    elif scelta==2:
        nome=input("inserisci nome:")
        cognome=input("inserisci cognome:")
        val=False
        for contatto in list:
            if contatto['nome']==nome and contatto['cognome']==cognome:
                print(contatto['numtel'])
                val=True
        if val==False:
            print("Utente non trovato")                
    elif scelta==3:
        nome=input("inserisci nome:")
        cognome=input("inserisci cognome:")
        val=False
        for contatto in list:
            if contatto['nome']==nome and contatto['cognome']==cognome:
                list.remove(contatto)
                val=True
            print(list)
        if val==False:
            print("Utente non trovato")
    elif scelta==4:
        numtel=input("inserisci numero di telefono:")
        val=False
        for contatto in list:
            if contatto['numtel']==numtel:
                print(contatto['nome']+" "+contatto['cognome'])
                val=True
        if val==False:
            print("Utente non trovato")
    