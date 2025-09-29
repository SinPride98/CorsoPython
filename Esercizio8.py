import random
import itertools


class carta:
    def __init__(self,seme,val):
        self.seme=seme
        self.val=val
        self.stringa=self.__str__()
    def __str__(self):
        return str(self.val)+" di "+self.seme
    def __repr__(self):
        # Cosa appare in liste, tuple, ecc.
        return f"{self.seme} {self.val}"  

def somma_presente(banco, carta_giocata):
    for r in range(2, len(banco)+1):
        for combo in itertools.combinations(banco, r):
            if sum(c.val for c in combo) == carta_giocata.val:
                #print(str(combo))
                return True, combo
    return False, None


listC=[]
listS=["denari","bastoni","spade","coppe"]

giocatore1=[]
giocatore2=[]
banco=[]
risultatoG1=[]
risultatoG2=[]
somme=[]

punteggioG1=0
punteggioG2=0

while punteggioG1<11 and punteggioG2<11:
    puntTur1=[]
    puntTur2=[]
    for s in listS:
        for v in range(1,11):
            card=carta(s,v)
            listC.append(card)
    random.shuffle(listC)

    for c in range(1,5):
        banco.append(listC.pop())

    while len(listC)!=0:
        for c in range(1,4):
            giocatore1.append(listC.pop())
            giocatore2.append(listC.pop())

        for c in range(1,4):
            print("Giocatore 1:")
            for g in giocatore1:
                print(g.__str__())
            print("\n")
            print("banco:")
            for c in banco:
                print(c.__str__())
            print("\n")
            cartaB=False
            try:
                if len(listC)!=0 and len(giocatore1)!=0:
                    scelta=int(input("Scegli la tua carta da 1 a 3:"))
                for b in banco :
                    if b.val==giocatore1[scelta-1].val:
                        risultatoG1.append(b)
                        banco.remove(b)
                        if len(banco)==0:
                            punteggioG1+=1
                            puntTur1.append("Scopa")
                        risultatoG1.append(giocatore1[scelta-1])
                        cartaB=True
                if cartaB==False:
                    cartaB,somme=somma_presente(banco,giocatore1[scelta-1])
                    if cartaB:
                        for s in somme:
                            risultatoG1.append(s)
                            banco.remove(s)
                            if len(banco)==0:
                                punteggioG1+=1
                                puntTur1.append("Scopa")
                    else:
                        banco.append(giocatore1[scelta-1])
                giocatore1.pop(scelta-1)
            except IndexError:
                print("\nScelta carta sbagliata!!\n")
                scelta=random.randint(1,len(giocatore1))
                #giocatore1[random.randint(1,len(giocatore1))]
                #banco.append(scelta)
                #giocatore1.remove(scelta)
                for b in banco :
                    if b.val==giocatore1[scelta-1].val:
                        risultatoG1.append(b)
                        banco.remove(b)
                        if len(banco)==0:
                            punteggioG1+=1
                            puntTur1.append("Scopa")
                        risultatoG1.append(giocatore1[scelta-1])
                        cartaB=True
                if cartaB==False:
                    cartaB,somme=somma_presente(banco,giocatore1[scelta-1])
                    if cartaB:
                        print(somme)
                        for s in somme:
                            risultatoG1.append(s)
                            banco.remove(s)
                            if len(banco)==0:
                                punteggioG1+=1
                                puntTur1.append("Scopa")
                    else:
                        banco.append(giocatore1[scelta-1])
                giocatore1.pop(scelta-1)

            scelta=random.randint(1,len(giocatore2))
            for b in banco :
                #print("giocatore 2 presente")
                if b.val==giocatore2[scelta-1].val:
                    risultatoG2.append(b)
                    banco.remove(b)
                    if len(banco)==0:
                        punteggioG2+=1
                        puntTur2.append("Scopa")
                    risultatoG2.append(giocatore2[scelta-1])
                    cartaB=True
            if cartaB==False:
                cartaB,somme=somma_presente(banco,giocatore2[scelta-1])
                if cartaB:
                    for s in somme:
                        risultatoG1.append(s)
                        banco.remove(s)
                        if len(banco)==0:
                            punteggioG2+=punteggioG2
                            puntTur2.append("Scopa")
                else:
                    banco.append(giocatore2[scelta-1])
            giocatore2.pop(scelta-1)


    if len(risultatoG1)<len(risultatoG2):
        punteggioG2+=1
        puntTur2.append("Numero di carte")
    elif len(risultatoG1)>len(risultatoG2):
        punteggioG1+=1
        puntTur1.append("Numero di carte")
    
    if "7 di denari" in risultatoG1:
        punteggioG1+=1
        puntTur1.append("7 di denari")
    else:
        punteggioG2+=1
        puntTur2.append("7 di denari")

    if sum(1 for c in risultatoG1 if c.val == 7)>sum(1 for c in risultatoG2 if c.val == 7):
        punteggioG1+=1
        puntTur1.append("primiera")
    elif sum(1 for c in risultatoG1 if c.val == 7)<sum(1 for c in risultatoG2 if c.val == 7):
        punteggioG2+=1
        puntTur2.append("primiera")
    
    if sum(1 for c in risultatoG1 if c.seme == "denari")>sum(1 for c in risultatoG2 if c.seme == "denari"):
        punteggioG1+=1
        puntTur1.append("carte denari")
    elif sum(1 for c in risultatoG1 if c.seme == "denari")<sum(1 for c in risultatoG2 if c.seme == "denari"):
        punteggioG2+=1
        puntTur2.append("carte denari")

    print(puntTur1)
    print(puntTur2)

if punteggioG1>punteggioG2:
    print("\nVittoria giocatore 1:",punteggioG1)
elif punteggioG2>punteggioG1:
    print("Vittoria giocatore 2:",punteggioG2)
else:
    print("Parita")

