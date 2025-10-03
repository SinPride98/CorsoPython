import  pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('Esercizio14/titanic.csv')
#print(df[df['Age']>40])
#data frame nuovo per ogni età da 10 a 60 numero di sopravvissuti e numero di morti
listAge=[i for i in range(10, 61)]
listAge.append(0)
dataf=pd.DataFrame(listAge, index=listAge, columns=['Age'])
dataf['Survived']=0
dataf['Dead']=0 
dataf['Total']=0
for k,v in df.iterrows():
    if pd.isna(v['Age'])==False:
        age=int(v['Age'])
        if age>=10 and age<=60:
            if v['Survived']==1:
                dataf.at[age,'Survived']+=1
            else:
                dataf.at[age,'Dead']+=1
            dataf.at[age,'Total']+=1
    else:
        if v['Survived']==1:
            dataf.at[0,'Survived']+=1
        else:
            dataf.at[0,'Dead']+=1
        dataf.at[0,'Total']+=1
#print(dataf)

dataUD=pd.DataFrame(listAge, index=listAge, columns=['Age'])
dataUD['Female']=0
dataUD['Male']=0

for k,v in df.iterrows():
    if pd.isna(v['Age'])==False:
        age=int(v['Age'])
        if age>=10 and age<=60:
            if v['Sex']=='male':
                dataUD.at[age,'Male']+=1
            else:
                dataUD.at[age,'Female']+=1
    else:
        if v['Sex']=='male':
            dataUD.at[0,'Male']+=1
        else:
            dataUD.at[0,'Female']+=1

print(dataUD)


plt.bar(dataUD['Age'],dataUD['Male'])
#plt.show()

plt.pie(dataUD['Male'], labels=dataUD['Age'], autopct="%1.1f%%")
