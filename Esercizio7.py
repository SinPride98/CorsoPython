# Classe Dipendente

class Dipendente:

    def __init__(self, stringa):

        l = stringa.strip().split(";")

        self.nome = l[0]

        self.ore = int(l[1])

        self.paga = float(l[2])

    def stipendio(self):

        return self.ore * self.paga

    def __str__(self):

        return f"{self.nome};{self.ore};{self.paga}"

 

# Percorso file

file_path = r"C:\Users\licit\OneDrive\Desktop\Riverloop\corso python\esercizio_dipendente\dipendenti.txt"

# Lettura dei dipendenti dal file

ldip = []

with open(file_path, "r", encoding="utf-8") as f:

    for linea in f:

        if linea.strip():  # ignora righe vuote

            ldip.append(Dipendente(linea))

# Loop principale

scelta = -1

while scelta != 0:

    print("\nMenu:")

    print("1 - Aggiungere dipendente")

    print("2 - Modificare ore")

    print("3 - Modificare paga")

    print("4 - Eliminare dipendente")

    print("5 - Visualizzare lista dipendenti")

    print("0 - Chiudere il programma")

    

    try:

        scelta = int(input("Inserire scelta: "))

    except ValueError:

        print("Valore non valido, inserire un numero.")

        continue

    if scelta == 1:

        nnome = input("Inserisci nome: ")

        try:

            nore = int(input("Inserisci ore: "))

            npaga = float(input("Inserisci paga oraria: "))

            ndip = Dipendente(f"{nnome};{nore};{npaga}")

            ldip.append(ndip)

            print(f"Dipendente {nnome} aggiunto.")

        except ValueError:

            print("Ore o paga non valide.")

    elif scelta == 2:

        nome = input("Inserisci nome da modificare: ")

        trovato = False

        for dip in ldip:

            if dip.nome == nome:

                trovato = True

                try:

                    dip.ore = int(input("Inserisci nuove ore: "))

                    print(f"Ore aggiornate per {nome}.")

                except ValueError:

                    print("Valore ore non valido.")

        if not trovato:

            print("Dipendente non trovato.")

    elif scelta == 3:

        nome = input("Inserisci nome da modificare: ")

        trovato = False

        for dip in ldip:

            if dip.nome == nome:

                trovato = True

                try:

                    dip.paga = float(input("Inserisci nuova paga: "))

                    print(f"Paga aggiornata per {nome}.")

                except ValueError:

                    print("Valore paga non valido.")

        if not trovato:

            print("Dipendente non trovato.")

    elif scelta == 4:

        nome = input("Inserisci nome da eliminare: ")

        iniziale = len(ldip)

        ldip = [dip for dip in ldip if dip.nome != nome]

        if len(ldip) < iniziale:

            print(f"Dipendente {nome} eliminato.")

        else:

            print("Dipendente non trovato.")

    elif scelta == 5:

        if not ldip:

            print("Lista dipendenti vuota.")

        for dip in ldip:

            print(f"{dip.nome} - Ore: {dip.ore}, Paga: {dip.paga}, Stipendio: {dip.stipendio()}")

# Salvataggio finale

with open(file_path, "w", encoding="utf-8") as f:

    for dip in ldip:

        f.write(str(dip) + "\n")

print("Programma terminato. File aggiornato.")