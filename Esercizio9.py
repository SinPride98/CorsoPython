from datetime import datetime

class libro:
    def __init__(self,stringa,titolo=None,autore=None,anno=None,disp=None,data=None):
        if titolo!=None:
            self.t=titolo
            self.a=autore
            self.an=anno
            self.d=disp
            self.dataD=data
        else:
            llibro=stringa.split(";")
            self.t=llibro[0]
            self.a=llibro[1]
            self.an=llibro[2]
            self.d=bool(llibro[3])
            self.dataD=(llibro[4])
    def __str__(self):
        return "Libro:"+self.t+self.a+self.an+str(self.d)+self.dataD
    def scrivi(self):
        return self.t+";"+self.a+";"+self.an+";"+str(self.d)+";"+str(self.dataD)+"\n"
    
def cerca(llb):
    tin=input("inserisci titolo o autore:")
    for l in llb:
        if l.t==tin or l.a==tin:
            return llb.index(l)
    print("libro non trovato")
    return -1

def salvaF(llb):
    f=open("C:/Users/Michael-PC/Desktop/file/libri.txt","w")
    for l in llb:
        f.write(l.scrivi())
    f.close

llibri=[]
llibristr=[]
f=open("C:/Users/Michael-PC/Desktop/file/libri.txt","a")
f.close()    
f=open("C:/Users/Michael-PC/Desktop/file/libri.txt","r")
r=f.read()
f.close
llibristr=r.split("\n")

for l in llibristr:
    if l=="":
        continue
    llibri.append(libro(l))
scelta=1
while scelta!=0:
    print("1 per cercare il libro, 2 cambia stato da disponibile a non, 3 inserisci un nuovo libro, 4 file report")

    scelta=int(input("Iserisci scelta:"))

    if scelta==1:
       lIn=cerca(llibri)
       if lIn!=-1:
           print (f"Libro trovato:{llibri[lIn]}")

    if scelta==2:
        lIn=cerca(llibri)
        if lIn!=-1:
            llibri[lIn].d=not llibri[lIn].d
            if llibri[lIn].d==False:
                dataT=datetime.now()
                llibri[lIn].dataD=dataT.strftime("%d/%m/%Y")
            else:
                llibri[lIn].dataD=None
            salvaF(llibri)

    if scelta==3:
        tit=input("inserisci titolo:")
        aut=input("inserisci autore:")
        anno=input("inserisci anno:")

        l=libro(None,tit,aut,anno,True)
        llibri.append(l)
        salvaF(llibri)

    if scelta==4:
        f=open("C:/Users/Michael-PC/Desktop/file/report.txt","w")
        f.write("Libri disponibli:\n")
        for l in llibri:
            if l.d==True:
                f.write(l.scrivi())
        f.write("Libri prestati:\n")
        for l in llibri:
            if l.d!=True:
                f.write(l.scrivi())        
        f.close()
    