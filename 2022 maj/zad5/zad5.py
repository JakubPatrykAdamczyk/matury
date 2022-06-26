from itertools import count
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


#5.2
