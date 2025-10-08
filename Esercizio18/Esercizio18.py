#file studenti.csv  con nome cognome e matricola, e  file voto.csv con voto preso e maatricola studente.
#da menu aggiungere,eliminare o selezionare uno studente(con indici).
# Una volta selezionato uno studente si puo aggiungere un voto,visualizzare la media dei voti.
import csv
import pandas as pd

class Studente:
    def __init__(self, nome, cognome, matricola):
        self.nome = nome
        self.cognome = cognome
        self.matricola = matricola
        self.voti = []

    def aggiungi_voto(self, voto):
        self.voti.append(voto)
    
def main():
    scelta=-1
    studenti = []

    while scelta != 0:
        print("\nMenu:")
        print("1. Aggiungi studente")
        print("2. Elimina studente")
        print("3. Seleziona studente")
        print("0. Esci")
        scelta = int(input("Scegli un'opzione: "))

        if scelta == 1:
            nome = input("Nome: ")
            cognome = input("Cognome: ")
            matricola = input("Matricola: ")
            studenti.append(Studente(nome, cognome, matricola))
            with open('studenti.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([nome,cognome,matricola])
            print("Studente aggiunto.")
        elif scelta == 2:
            df=pd.read_csv('studenti.csv',header=None)
            index=int(input(f"Scegli l'indice dello studente da eliminare (0-{len(df)-1}): "))
            df=df.drop(index)
            df.to_csv('studenti.csv',header=False,index=False)
            print("Studente eliminato.")
        
        elif scelta == 3:
            df=pd.read_csv('studenti.csv',header=None)
            index=int(input(f"Scegli l'indice dello studente da selezionare (0-{len(df)-1}): "))
            studente_selezionato = Studente(df.iloc[index,0], df.iloc[index,1], df.iloc[index,2])
            scelta_studente=-1
            while scelta_studente != 0:
                print(f"\nStudente selezionato: {studente_selezionato.nome} {studente_selezionato.cognome}")
                print("1. Aggiungi voto")
                print("2. Visualizza media voti")
                print("0. Torna al menu principale")
                scelta_studente = int(input("Scegli un'opzione: "))

                if scelta_studente == 1:
                    voto = float(input("Inserisci il voto: "))
                    studente_selezionato.aggiungi_voto(voto)
                    with open('voti.csv', mode='a', newline='') as file:
                        writer = csv.DictWriter(file, fieldnames=["matricola","voto"])
                        if file.tell()==0:
                            writer.writeheader()
                        writer.writerow({"matricola":studente_selezionato.matricola,"voto":voto})
                    print("Voto aggiunto.")
                elif scelta_studente == 2:
                   dfV=(pd.read_csv('voti.csv'))
                   print(dfV[dfV["matricola"] == studente_selezionato.matricola]["voto"].mean())
                
main()                      
                            

        
        
