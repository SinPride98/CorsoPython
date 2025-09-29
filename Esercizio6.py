class dipendente:
    def __init__(self,nome,paga_oraria,ore_lavorate):
        self.nome=nome
        self.paga_oraria=float(paga_oraria)
        self.ore_lavorate=int(ore_lavorate)
    def stipendio(self):
        return self.paga_oraria*self.ore_lavorate
    def _str_(self):
        return self.nome+" "+str(self.paga_oraria)+" "+str(self.ore_lavorate)
    
 


f=open("C:/Users/Michael-PC/Desktop/file/Esercizio6.txt","r")
r=f.read()
f.close()
ldip=r.split("\n")
#count=0
#pOr=""
#for dip in ldip:
    #for d in dip:
        #if d.isalpha():
            #name+=d
        #elif d.isspace():
            #count=1
        #elif d.isdigit():
            #count=0
            #pOr+=d
        #elif d==".":
            #pOr+=d
        #elif d.isdigit() and count==1:
            #orL+=d
    



scelta=1
while scelta!=0:
    scelta=int(input("inserisci scelta:"))
    if scelta==1:
        nome=input("inserisci nome :")
        pOraria=float(input("inserisci paga oraria:"))
        oLav=int(input("inserisci ore lavorate:"))
        d=dipendente(nome,pOraria,oLav)
        ldip.append(d._str_())
    if scelta==2:
        nome = input("inserisci il nome per cambiare paga oraria: ")
        i = 0
        trovato = False
        for dip in ldip:
            name = ""
            pOr = ""
            orL = ""
            count = 0
            for d in dip:
                if count == 0:  # nome
                    if d.isalpha() or d == " ":
                        name += d
                    elif d.isdigit() or d == ".":
                        count = 1
                        pOr += d
                elif count == 1:  # paga
                    if d.isdigit() or d == ".":
                        pOr += d
                    elif d.isspace():
                        count = 2  # spazio dopo la paga → passiamo alle ore
                elif count == 2:  # ore
                    if d.isdigit():
                        orL += d
            name = name.strip()  # rimuove spazi iniziali/finali
            if name == nome:
                trovato = True
                break
            i += 1
        if trovato:
            try:
                nuovaPaga = float(input("Inserisci nuova paga oraria: "))
                d = dipendente(name, nuovaPaga, int(orL))
                ldip[i] = d._str_()  # ❇️ chiamato come funzione
                print(f"Paga aggiornata per {name}")
            except ValueError:
                print("Errore: paga o ore non valide.")
        else:
            print(f"Nessun dipendente trovato con nome '{nome}'")

    if scelta==3:
        nome = input("inserisci il nome per cambiare orario di lavoro: ")
        i = 0
        trovato = False
        for dip in ldip:
            name = ""
            pOr = ""
            orL = ""
            count = 0
            for d in dip:
                if count == 0:  # nome
                    if d.isalpha() or d == " ":
                        name += d
                    elif d.isdigit() or d == ".":
                        count = 1
                        pOr += d
                elif count == 1:  # paga
                    if d.isdigit() or d == ".":
                        pOr += d
                    elif d.isspace():
                        count = 2  # spazio dopo la paga → passiamo alle ore
                elif count == 2:  # ore
                    if d.isdigit():
                        orL += d
            name = name.strip()  # rimuove spazi iniziali/finali
            if name == nome:
                trovato = True
                break
            i += 1
        if trovato:
            try:
                nuovOrario = int(input("Inserisci nuovo orario: "))
                d = dipendente(name, float(pOr),nuovOrario)
                ldip[i] = d._str_()  # ❇️ chiamato come funzione
                print(f"ore aggiornata per {name}")
            except ValueError:
                print("Errore: paga o ore non valide.")
        else:
            print(f"Nessun dipendente trovato con nome '{nome}'")
    
    if scelta==4:
        nome = input("inserisci il nome da eliminare: ")
        i = 0
        trovato = False
        for dip in ldip:
            name = ""
            pOr = ""
            orL = ""
            count = 0
            for d in dip:
                if count == 0:  # nome
                    if d.isalpha() or d == " ":
                        name += d
                    elif d.isdigit() or d == ".":
                        count = 1
                        pOr += d
                elif count == 1:  # paga
                    if d.isdigit() or d == ".":
                        pOr += d
                    elif d.isspace():
                        count = 2  # spazio dopo la paga → passiamo alle ore
                elif count == 2:  # ore
                    if d.isdigit():
                        orL += d
            name = name.strip()  # rimuove spazi iniziali/finali
            if name == nome:
                trovato = True
                break
            i += 1
        if trovato:
            try:
                #d= dipendente(name, float(pOr),int(orL))
                ldip.pop(i)
                print(f"eimininato {name}")
            except ValueError:
                print("Errore: eliminazione fallita")
        else:
            print(f"Nessun dipendente trovato con nome '{nome}'")
    if scelta==5:
        f=open("C:/Users/Michael-PC/Desktop/file/Esercizio6.txt","w")
        for dip in ldip:
            name=""
            pOr=""
            orL=""
            count=0
            for d in dip:
                if count == 0:  # nome
                    if d.isalpha() or d == " ":
                        name += d
                    elif d.isdigit() or d == ".":
                        count = 1
                        pOr += d
                elif count == 1:  # paga
                    if d.isdigit() or d == ".":
                        pOr += d
                    elif d.isspace():
                        count = 2  # spazio dopo la paga → passiamo alle ore
                elif count == 2:  # ore
                    if d.isdigit():
                        orL += d
            f.write(name+" "+pOr+" "+orL+"\n")
        f.close()
print("programma terminato")
        
