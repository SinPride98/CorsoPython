"""Facciamo intanto degli esercizi riepilogativi, iniziamo da questo: Scrivi il seguente programma:

1 Utilizzando la funzione input chiedi all'utente:

	"anno di nascita" (nel formato "YYYY"), assegna l'input ottenuto ad una variabile "anno_di_nascita"

	"anno corrente" (nel formato "YYYY", esempio 2021) e assegna l'input ottenuto ad una variabile "anno_corrente"

2. Calcola l'età dell'utente e assegnala ad una variabile "age" (attenzione al datatype che resituisce la funzione input...)

3. Stampa "age" """

import datetime

anno=int(input("inserisci il tuo anno di nascita:"))
data_nascita = datetime.datetime(anno, 1, 1)
anno_corrente=datetime.datetime.now()
age=anno_corrente.year-data_nascita.year
print(f"i tuoi anni sono: {age}")