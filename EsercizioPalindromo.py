# Scrivi una funzione func che controlla se la parola che viene passata come argomento è un palindromo,cioè se letta in senso inverso mantiene immutato il significato

def func(stringa):
    stringa_invertita = stringa[::-1]
    if stringa.lower()==stringa_invertita.lower():
        return "Palindroma"
    else:
        return "Non palindroma"
    
varchar=input("inserisci la tua parola:")

print(f"la tua parola è:{func(varchar)}")