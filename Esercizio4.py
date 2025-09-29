#7-11 vinci
#2-3 perddi
#altri cas rilanci

import random

class giocatore:
    def lancio(self):
        dado=random.randint(2,12)
        return dado
    

g1=giocatore()
lancio1=g1.lancio()
print(lancio1)

g2=giocatore()
lancio2=g2.lancio()
print(lancio2)

if lancio1>lancio2:
    print("vittoria giocatore 1")
else:
    print("vittoria giocatore 2")

