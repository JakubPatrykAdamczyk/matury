import os
mypath=os.getcwd()
mypath+="\\matury\\"
mypath+="2021 maj\zad4"
f=open(mypath+"\\instrukcje.txt")

pol=[]
co=[]
for i in f:
    n=0    
    for w in i.split():
        w=w.strip()
        if n==0: 
            pol.append(w)
            n+=1
        elif n==1:  
            co.append(w)

# # 4.1
# li=0
# for i in range(len(pol)):
#     if "DOPISZ"==pol[i]:
#         li+=1
#     if "USUN"==pol[i]:
#         li-=1
# print("Dlugość na koniec "+str(li))

# # 4.2
# n_max=0
# w_last=""
# w_max=""
# n_now=0
# for i in range(len(pol)):
#     if w_last==pol[i]:
#         n_now+=1
#     else:
#         n_now=1
#         w_last=pol[i]
#     if n_max<n_now:
#         n_max=n_now
#         w_max=w_last
# print("rodzaj instrukcji- "+str(w_max)+", dlugosc: "+str(n_max))

# 4.3

    
