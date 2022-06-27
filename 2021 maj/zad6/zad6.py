import os
from traceback import print_stack


mypath=os.getcwd()
mypath+="\\matury\\"
mypath+="2021 maj\zad6"
u=open(mypath+"\\gracze.txt")
g_IdGracza=[]
g_Kraj=[]
g_DataDoloczenia=[]

for i in u:
    n=0
    for w in i.split("\t"):
        if n==0:
            w=w.strip()
            g_IdGracza.append(w) 
            n+=1
        elif n==1:
            w=w.strip()
            g_Kraj.append(w) 
            n+=1            
        elif n==2:
            w=w.strip()
            g_DataDoloczenia.append(w) 
            n+=1
            w=w.strip()
       


k=open(mypath+"\jednostki.txt")
j_IdJednostki=[]
j_IdGracza=[]
j_Nazwa=[]
j_LokX=[]
j_LokY=[]
for i in k:
    n=0
    for w in i.split("\t"):
        if n==0:
            w=w.strip()
            j_IdJednostki.append(w) 
            n+=1
        elif n==1:
            w=w.strip()
            j_IdGracza.append(w) 
            n+=1
        elif n==2:
            w=w.strip()
            j_Nazwa.append(w) 
            n+=1    
        elif n==3:
            w=w.strip()
            j_LokX.append(w) 
            n+=1  
        elif n==4:
            w=w.strip()
            j_LokY.append(w) 
            n+=1 

e=open(mypath+"\klasy.txt")
k_nazwa=[]
k_sila=[]
k_strzal=[]
k_magia=[]
k_szybkosc=[]
for i in e:
    n=0
    for w in i.split("\t"):
        if n==0:
            w=w.strip()
            k_nazwa.append(w) 
            n+=1
        elif n==1:
            w=w.strip()
            k_sila.append(w) 
            n+=1            
        elif n==2:
            w=w.strip()
            k_strzal.append(w) 
            n+=1
            w=w.strip()
        elif n==3:
            w=w.strip()
            k_magia.append(w) 
            n+=1
        elif n==4:
            w=w.strip()
            k_szybkosc.append(w) 
            n+=1


# # zad6.1
# l={}
# for i in range (1,len(g_IdGracza)):
#     l[g_Kraj[i]]=0
# print(str(g_DataDoloczenia[1][0:4]))
# for i in range (1,len(g_IdGracza)):
#     if int(g_DataDoloczenia[i][0:4])==2018:
#         n=int(l[g_Kraj[i]])
#         n+=1
#         l[g_Kraj[i]]=n
# ans=sorted(l.items(),key=lambda x: x[1],reverse=True)
# for i in range(5):
#     print(ans[i])

# # zad6.2
# st=0
# for i in range(1,len(k_nazwa)):
#     s=k_nazwa[i]
    
#     for x in range (len(s)):
#         if s[x:].startswith("elf"):
#             st+=int(k_strzal[i])
# print(st)


# # zad6.3
# t=[]
# for i in g_IdGracza:
#     t.append(i)

# for i in range(1,len(j_IdJednostki)):
#     if j_Nazwa[i]=="artylerzysta":        
#         for j in range(1,len(t)):
#             if str(t[j])==str(j_IdGracza[i]):
#                 t.remove(j_IdGracza[i])
#                 break

# print(str(t))

# # zad6.4
# l={}
# for i in range(1,len(k_nazwa)):
#     l[k_nazwa[i]]=0
# for i in range(1,len(j_IdJednostki)):
#     szyb=0
    
#     for j in range (1,len(k_nazwa)):
#         if j_Nazwa[i]==k_nazwa[j]:
#             szyb=int(k_szybkosc[j])
#             break
#     if pow((100-int(j_LokX[i])),2)+pow((100-int(j_LokY[i])),2)<=pow(szyb,2):
#         n=int(l[j_Nazwa[i]])
#         n+=1
#         l[j_Nazwa[i]]=n
# print(l)

# zad6.5
bit=0
pl=0
for i in range(1,len(j_IdJednostki)):
    for j in range(i,len(j_IdJednostki)):
        if j_LokX[i]==j_LokX[j] and j_LokY[i]==j_LokY[j] and j_IdGracza[i]!=j_IdGracza[j]:
            bit+=1
            for g in range(1,len(g_IdGracza)):
                if (j_IdGracza[i]==g_IdGracza[g] and g_Kraj[g]=="Polska") or (j_IdGracza[j]==g_IdGracza[g] and g_Kraj[g]=="Polska"):
                    pl+=1
                    break


print(bit)
print(pl)