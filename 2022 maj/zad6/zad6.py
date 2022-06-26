import os


mypath=os.getcwd()
mypath+="\\matury\\"
mypath+="2022 maj\zad6"
u=open(mypath+"\\uczen.txt")
u_IdUcznia=[]
u_Imie=[]
u_Nazwisko=[]
u_IdKlasy=[]
for i in u:
    n=0
    for w in i.split(";"):
        if n==0:
            w=w.strip()
            u_IdUcznia.append(w) 
            n+=1
        elif n==1:
            w=w.strip()
            u_Imie.append(w) 
            n+=1            
        elif n==2:
            w=w.strip()
            u_Nazwisko.append(w) 
            n+=1
            w=w.strip()
        elif n==3:
            w=w.strip()
            u_IdKlasy.append(w) 
            n+=1


k=open(mypath+"\klasa.txt")
k_IdKlasy=[]
k_ProfilKlasy=[]
for i in k:
    n=0
    for w in i.split(";"):
        if n==0:
            w=w.strip()
            k_IdKlasy.append(w) 
            n+=1
        elif n==1:
            w=w.strip()
            k_ProfilKlasy.append(w) 
            n+=1    

e=open(mypath+"\ewidencja.txt")
e_IdEwidencji=[]
e_IdUcznia=[]
e_Wejscie=[]
e_Wyjscie=[]

for i in e:
    n=0
    for w in i.split(";"):
        if n==0:
            w=w.strip()
            e_IdEwidencji.append(w) 
            n+=1
        elif n==1:
            w=w.strip()
            e_IdUcznia.append(w) 
            n+=1            
        elif n==2:
            w=w.strip()
            e_Wejscie.append(w) 
            n+=1
            w=w.strip()
        elif n==3:
            w=w.strip()
            e_Wyjscie.append(w) 
            n+=1


# # 6.1
# c=0
# for i in range(1,len(e_IdUcznia)):
#     if "a"==u_Imie[int(e_IdUcznia[i])][-1]:
#         for j in range(1,len(k_IdKlasy)):
#             if u_IdKlasy[int(e_IdUcznia[i])]==k_IdKlasy[j]:
#                 if k_ProfilKlasy[j]=="biologiczno-chemiczny":
#                     c+=1
# print(c)


# #6.2
# d_old=""
# l={}
# z=0
# for i in range(1,len(e_IdEwidencji)):
#     if d_old==e_Wejscie[i][0:10]:
#         if "07"==e_Wejscie[i][11:13]:
#             z+=1
#             l[d_old]=z
#     else:
#         d_old=e_Wejscie[i][0:10]
#         z=0

# print(l)


# 6.4
t=[]
for i in u_IdUcznia:
    t.append(i)

for i in range(1,len(e_IdEwidencji)):
    if e_Wejscie[i][0:10]=="2022-04-06":        
        for j in range(1,len(t)):
            if str(t[j])==str(e_IdUcznia[i]):
                t.remove(e_IdUcznia[i])
                break
for i in  range(len(t)):
    print(str(u_Imie[i])+" "+str(u_Nazwisko[i]))
 
