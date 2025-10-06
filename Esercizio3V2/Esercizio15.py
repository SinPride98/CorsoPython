#magazzino versione ddatabase
import mysql.connector

db=mysql.connector.connect(host="localhost",user="root",password="",database="prova")
cursor=db.cursor()

cursor.execute("CREATE TABLE Magazzino (id INT AUTO_INCREMENT PRIMARY KEY, nomeP VARCHAR(255), quantita INT, prezzo FLOAT)")

scelta =1

while scelta !=0:

    print("1) Inserisci prodotto")
    print("2) Cerca proodotto")
    print("3) Cambia quantita")
    print("4) Cambia prezzo")
    print("0) Esci")
    scelta=int(input("Scelta: "))
    
    if scelta==1:
        nome=input("Nome prodotto: ")
        quantita=int(input("Quantita: "))
        prezzo=float(input("Prezzo: "))
         
        sql="INSERT INTO Magazzino (nomeP, quantita, prezzo) VALUES (%s, %d, %f)"
        valore=(nome, quantita, prezzo)
        cursor.execute(sql,valore)
        db.commit()
    
    elif scelta==2:
        nome=input("Nome prodotto da cercare: ")
        sql="SELECT quantita,prezzo FROM Magazzino WHERE nomeP=%s"
        valore=(nome,)
        cursor.execute(sql,valore)
        result=cursor.fetchall()
        for x in result:
            print("Quantita: ",x[0]," Prezzo: ",x[1])
    
    elif scelta==3:
        nome=input("Nome prodotto da cambiare quantita: ")
        quantita=int(input("Nuova quantita: "))
        sql="UPDATE Magazzino SET quantita=%d WHERE nomeP=%s"
        valore=(quantita,nome)
        cursor.execute(sql,valore)
        db.commit()

    elif scelta==4:
        nome=input("Nome prodotto da cambiare prezzo: ")
        prezzo=float(input("Nuovo prezzo: "))
        sql="UPDATE Magazzino SET prezzo=%f WHERE nomeP=%s"
        valore=(prezzo,nome)
        cursor.execute(sql,valore)
        db.commit()

    

        
        
