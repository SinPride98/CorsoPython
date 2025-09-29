import csv

listD=[]

file_path= r"C:\Users\Michael-PC\Desktop\file\dipendenti.csv" 
f=open(file_path,"a",newline='')
f.close()  

with open(file_path,"r") as f:
    reader=csv.DictReader(f)
    for dip in reader:
        listD.append(dip)

scelta=1
while scelta!=0:
    scelta=int(input("Inserisci la tua scelta:"))
    if scelta==1:
        nomeD=input("inserisci il nome del dipendente:")
        ore_lavorate=int(input("inserisci le ore lavorate:"))
        paga_oraria=int(input("Inserisci lla paga oraraia:"))

        with open(file_path,"w",newline='') as f:
            fieldnames=["nome","ore_lavorate","paga_oraria"]
            writer=csv.DictWriter(f,fieldnames=fieldnames)
            writer.writeheader()
            listD.append({"nome":nomeD,"ore_lavorate":ore_lavorate,"paga_oraria":paga_oraria})
            writer.writerows(listD) 
    
    elif scelta==2:
        nomeD=input("inserisci il nome del dipendente:")
        for dip in listD:
            if dip["nome"]==nomeD:
               listD.remove(dip)
        with open(file_path,"w",newline='') as f:
            fieldnames=["nome","ore_lavorate","paga_oraria"]
            writer=csv.DictWriter(f,fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(listD)
    
    elif scelta==3:
        nomeD=input("inserisci il nome del dipendente:")
        for dip in listD:
            if dip["nome"]==nomeD:
                print(dip)
            else:
                print("dipendente non trovato")
    
    elif scelta==4:
        for dip in listD:
            print(dip)

    

