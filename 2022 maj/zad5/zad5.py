from itertools import count
import plotly.express as px
import os

mypath=os.getcwd()
mypath+="\\matury\\"
mypath+="2022 maj\zad5"
f=open(mypath+"\soki.txt")

# t=[]
id=[]
dat=[]
city=[]
big=[]

for i in f:
    n=0
    for w in i.split():
        if n==0:
            w=w.strip()
            id.append(w) 
            n+=1
        elif n==1:
            w=w.strip()
            dat.append(w) 
            n+=1            
        elif n==2:
            w=w.strip()
            city.append(w) 
            n+=1
            w=w.strip()
        elif n==3:
            big.append(w) 
            n+=1


# #5.1
# print("Gniezno: " + str(city.count("Gniezno")))
# print("Malbork: " + str(city.count("Malbork")))
# print("Ogrodzieniec: " + str(city.count("Ogrodzieniec")))
# print("Przemysl: " + str(city.count("Przemysl")))


# #5.2
# a=50
# l=0
# ln=0
# st_dt=""
# st_dtn=""
# ed_dt=""
# ed_dtn=""
# for i in range(len(city)):
#     if "Ogrodzieniec"==city[i]:
#         if (a+1)==int(dat[i][0:2]):
#             # print(dat[i][0:2])
#             ln+=1
#             ed_dtn=dat[i]
#         else:
#             ln=0
#             st_dtn=dat[i]
#         a=int(dat[i][0:2])
#         if ln>l:
#             l=ln
#             st_dt=st_dtn
#             ed_dt=ed_dtn
# print (l)
# print("od "+st_dt+" do "+ed_dt)

# #5.3
# gn=0
# ma=0
# ogr=0
# prz=0
# for i in range (len(city)):
#     if "Gniezno"==city[i]: gn+=int(big[i])
#     if "Malbork"==city[i]: ma+=int(big[i])
#     if "Ogrodzieniec"==city[i]: ogr+=int(big[i])
#     if "Przemysl"==city[i]: prz+=int(big[i])

# print("Gniezno: " + str(gn))
# print("Malbork: " + str(ma))
# print("Ogrodzieniec: " + str(ogr))
# print("Przemysl: " + str(prz))


 
# labels = ['Gniezno','Malbork','Ogrodzieniec','Przemysl']
# values = [gn, ma, ogr, prz]
 
# fig = px.pie(values=values, names=labels,color_discrete_sequence=px.colors.sequential.RdBu)
 
# fig.show()
        