"""Crea un dataframe avente una colonna "nomi" e tre colonne aventi i voti in centesimi in "matematica" "informatica" e "inglese". 
Crea una funzione che calcoli la media tra questi voti per ciascun allievo. (numero righe: 5)"""


import pandas as pd
import statistics as stat

def calcola_media(row):

    voti = [row["matematica"], row["informatica"], row["inglese"]]

    return round(stat.mean(voti))

def insuf(riga):  
    if  riga["media"]>80:
        return "Ottimo"
    elif riga["media"]>60:
        return "Buono"
    else:
        return "Insufficiente"


df = pd.DataFrame({

    "nomi": ["Alice", "Marco", "Giulia", "Luca", "Sara"],

    "matematica": [30, 92, 78, 88, 95],

    "informatica": [90, 87, 82, 91, 89],

    "inglese": [88, 79, 85, 93, 90]

  })
df["media"] = df.apply(calcola_media, axis=1)
df["Descrizione media"]=df.apply(insuf,axis=1)

print(df)


