#Crea una classe ArchivioStudenti che gestisce:aggiunta di studenti,salvataggio su database SQL,caricamento da dataabse SQL.

import mysql.connector

class ArchivioStudenti:
    def __init__(self, db_name, user, password, host='localhost'):
        self.db =mysql.connector.connect(user=user, password=password, host=host, database=db_name)
        self.cursor = self.db.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS studenti (
                                id INT AUTO_INCREMENT PRIMARY KEY,
                                nome VARCHAR(100),
                                cognome VARCHAR(100),
                                eta INT)''')
    
    def aggiungi_studente(self, nome, cognome, eta):
        query = "INSERT INTO studenti (nome, cognome, eta) VALUES (%s, %s, %s)"
        self.cursor.execute(query, (nome, cognome, eta))
        self.db.commit()
    
    def carica_studenti(self):
        query = "SELECT * FROM studenti"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def chiudi(self):
        self.cursor.close()
        self.db.close()


# Esempio di utilizzo
if __name__ == "__main__":
    archivio = ArchivioStudenti(db_name='prova', user='root', password='')
    scelta=-1
    while scelta!=0:
        print("1. Aggiungi studente")
        print("2. Visualizza studenti")
        print("0. Esci")
        scelta=int(input("Scegli un'opzione: "))
        if scelta==1:
            nome=input("Nome: ")
            cognome=input("Cognome: ")
            eta=int(input("Età: "))
            archivio.aggiungi_studente(nome, cognome, eta)
        elif scelta==2:
            studenti = archivio.carica_studenti()
            for studente in studenti:
                print(studente)
        elif scelta==0: 
            archivio.chiudi()
            print("Uscita...")
        else:
            print("Scelta non valida.")

   

 


 



 

