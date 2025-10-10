"""Crea una semplice interfaccia grafica che permetta all’utente di inserire:
Il prezzo originale di un prodotto
La percentuale di sconto
Un pulsante per calcolare il prezzo scontato
Un'etichetta che mostra il prezzo finale

🧩 Requisiti:
Usa CTkEntry per i campi di input
Usa CTkButton per il calcolo
Usa CTkLabel per mostrare il risultato
Aggiungi un po’ di stile con pack() o grid() e pady

💡 Bonus (facoltativi):
Aggiungi un CTkCheckBox per includere o escludere l’IVA (22%)
Aggiungi un CTkRadioButton per scegliere tra due valute: euro o dollari
Mostra un messaggio di errore se l’input non è valido"""




import customtkinter as tk

def validate_input(*args):
    valueP = entryP_var.get()
    valueS=entryS_var.get()
    if not valueP.isdigit():
        entryP_var.set(''.join(filter(str.isdigit, valueP)))
    if not valueS.isdigit():
        entryS_var.set(''.join(filter(str.isdigit, valueS)))


def calcola_sconto():
    # logica per calcolare il prezzo scontato
    prezzo=entryP.get()
    sconto=entryS.get()
    prezzoScontato=int(prezzo)-((int(sconto)/100)*int(prezzo))
    label.configure(text=f"Prezzo Scontato:{prezzoScontato}")

app = tk.CTk()
app.title("Calcolatrice di Sconti")
app.geometry("370x250")
# Entry per prezzo originale
labelP=tk.CTkLabel(app,text="Insserisci Prezzo:")
labelP.grid(row=0,column=0,pady=20,padx=20)

labelS=tk.CTkLabel(app,text="Inserisci Sconto:")
labelS.grid(row=0,column=1,pady=20,padx=20)

entryP_var = tk.StringVar()
entryP_var.trace_add("write", validate_input)
entryP = tk.CTkEntry(app,textvariable=entryP_var)
entryP.grid(row=1,column=0,padx=20)

# Entry per percentuale di sconto
entryS_var = tk.StringVar()
entryS_var.trace_add("write", validate_input)
entryS = tk.CTkEntry(app,textvariable=entryS_var)
entryS.grid(row=1,column=1,padx=20)

# Button per calcolare
button = tk.CTkButton(app, text="Calcola Sconto",command=calcola_sconto)
button.grid(row=2,column=0,pady=20,padx=20,columnspan=2)
# Label per mostrare il risultato
label = tk.CTkLabel(app, text="", fg_color="transparent")
label.grid(row=3,column=0,pady=20,padx=20,columnspan=2)

app.mainloop()