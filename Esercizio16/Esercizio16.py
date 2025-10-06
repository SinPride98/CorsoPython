#trasformare un database mysql in python in un csv e viceversa

import csv
import mysql.connector


db=mysql.connector.connect(host="localhost",user="root",password="",database="prova")
cursor=db.cursor()

#cursor.execute("CREATE TABLE Pokemon (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), type1 VARCHAR(255), type2 VARCHAR(255), total INT, hp INT, attack INT, defense INT, sp_atk INT, sp_def INT, speed INT, generation INT, legendary BOOLEAN)")

with open(r"C:\Users\Michael-PC\Desktop\Progetti\CorsoPython\Esercizio16\pokemon.csv","r") as f:
    reader=csv.reader(f)
    next(reader) #salta la prima riga
    for row in reader:
        row.pop(0)
        cursor.execute("INSERT INTO Pokemon (nome, type1, type2, total, hp, attack, defense, sp_atk, sp_def, speed, generation, legendary) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",row)
    db.commit()

cursor.execute("SELECT * FROM Pokemon")
result=cursor.fetchall()
with open(r"C:\Users\Michael-PC\Desktop\Progetti\CorsoPython\Esercizio16\pokemon_from_db.csv","w",newline='') as f:
    for riga in result:
        writer=csv.writer(f)
        writer.writerow(riga)  
f.close()
