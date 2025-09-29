f=open("C:/Users/Michael-PC/Desktop/file/esercizio5.txt","r")
str1=f.read()
f.close()

l=str1.split("\n")

f=open("C:/Users/Michael-PC/Desktop/file/esercizio5alternative.txt","w")
count=1
for div in l:
    c=str(count)
    f.write(c+div+"\n")
    count+=1
f.close()