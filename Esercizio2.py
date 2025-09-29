#in ascii da 97 a 122 sono lettere minuscole. 2 funzioni : ord(restituisce caratttere in ascii) e chr(dda ascii a carattere).

def crit(chiave,frase):
    val=0
    fraseC=""
    for char in frase:
        val=ord(char)
        if val>=97 and val<=122:
            val+=chiave
            if val<=122:
                char=chr(val)
            else:
                val=val-24
                char=chr(val)
        fraseC+=char
    return fraseC

def decri(chiave,frase):
    val=0
    fraseD=""
    for char in frase:
        val=ord(char)
        if val>=97 and val<=122:
            val=val-chiave
            if val>=97:
                char=chr(val)
            else:
                val=val+24
                char=chr(val)
        fraseD+=char
    return fraseD

scelta=1
str=""
c=int(input("inserisci chiave:"))
while scelta!=0:
    print(str)
    scelta=int(input("inserisci scelta:"))
    if scelta==1:
        f=open("C:/Users/Michael-PC/Desktop/file/prova.txt","r")
        frase=f.read()
        f.close()
        str=crit(c,frase)
        f=open("C:/Users/Michael-PC/Desktop/file/prova.txt","w")
        f.write(str)
        f.close()
    elif scelta==2:
        f=open("C:/Users/Michael-PC/Desktop/file/prova.txt","r")
        frase=f.read()
        f.close()
        str=decri(c,frase)
        f=open("C:/Users/Michael-PC/Desktop/file/prova.txt","w")
        f.write(str)
        f.close()
    