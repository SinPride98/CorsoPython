"""
in python è possibile interfacciarsi ai database tramite mysql.
-cos'è un database?
è un insieme organizzato di dati memorizzati in modo da poter essere facilmente accessi, gestiti e aggiornati da programmi o utenti.
-cos'è mysql?
è un sistema di gestione di database relazionali (RDBMS), cioè un programma che permette di creare, gestire e interrogare database
basati su tabelle collegate tra loro tramite relazion

passo 1)
scaricare xampp(win) o mampp(mac) e mysql community
passo 2)
 installare i driver -> pip install mysql-connector-python
passo 3)
importare la libreria e creare l'oggetto   
"""
import mysql.connector
db =mysql.connector.connect(host="localhost",user="root",password="",database="prova")
"""passo 4)creare il cursore"""
cursor=db.cursor()
"""
tramire cursor.execute possiamo passare da parametro il comando sql che desideriamo"""
#CREATE -> CREARE TABELLE
cursor.execute("CREATE TABLE nome (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), cognome VARCHAR(255))")
#INSERT
sql="INSERT INTO nome (nome, cognome) VALUES (%s, %s)"
valore=("Mario","Rossi")
cursor.execute(sql,valore)
db.commit() #serve per confermare 
#INSERT MULTIPLO 
valori=[
    ("giovanni","storti"),
    ("piero","pelù"),
    ("peter","pan")
]
cursor.executemany(sql,valori)
db.commit() 
#SELECT
select="SELECT * FROM nome"
cursor.execute(select)
risultato=cursor.fetchall()

for riga in risultato:
    print(riga)

selectwhere="SELECT * FROM nome WHERE nome='piero'"
cursor.execute(selectwhere)
risultato=cursor.fetchall()

for riga in risultato:
    print(riga)

    
selectorder="SELECT * FROM nome ORDER BY nome"
cursor.execute(selectorder)
risultato=cursor.fetchall()

for riga in risultato:
    print(riga)
