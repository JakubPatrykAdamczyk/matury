import os
import matplotlib.pyplot as plt

mypath=os.getcwd()
mypath+="\\matury\\"
mypath+="2021 maj\zad5"
f=open(mypath+"\\wodociagi.txt")

l={}
t=[]
wt=[]
word=""
for i in f:
    n=0
    
    for w in i.split(";"):
        w=w.strip()
        if n%13==0:            
            word=w
            wt.append(w)
            n+=1
        else:
            n+=1
            t.append(w)
        if n%13==0:
            l[word]=t
            del t
            t=[]

# # 5.1
# mz={}
# # print(list(l.keys())[5])
# for i in range (1,len(wt)):
#     n=0
#     for j in range(12):
#         n+=int(l[wt[i]][j])
#     n=n/12
#     mz[list(l.keys())[i]]=n

# # for i in range(10):

# #     print(list(mz.items())[len(mz)-i-1])
# ans=sorted(mz.items(),key=lambda x: x[1],reverse=True)

# for i in range(10):
#     print(ans[i])

# # 5.2
# dziel={}
# print(wt[1][7:10])
# for i in range(1,len(wt)):
#     dziel[wt[i][7:10]]=0
# for i in range(1,len(wt)):
#     n=0
#     for j in range(12):
#         n+=int(l[wt[i]][j])
#     n+=dziel[wt[i][7:10]]
#     dziel[wt[i][7:10]]=n
# print(dziel)

# # 5.3
# dziel={}
# # print(wt[1][7:10])
# for i in range(1,len(wt)):
#     dziel[wt[i][7:10]]=[0,0,0,0,0,0,0,0,0,0,0,0]
# for i in range(1,len(wt)):
#     t=[]
#     for j in range(12):
#         n=0
#         n+=int(l[wt[i]][j])
#         n+=int(dziel[wt[i][7:10]][j])
#         t.append(n)
    
#     dziel[wt[i][7:10]]=t
#     del t
# dzielmax={}
# for i in range(1,len(wt)):
#    dzielmax[wt[i][7:10]]=0 
# for i in range(1,len(wt)):
#     nm=0
    
#     for j in range(12):
#         nn=int(dziel[wt[i][7:10]][j])
#         if nm<nn:nm=nn
#     dzielmax[wt[i][7:10]]=nn
# print(dzielmax)


# # 5.4
# mon=[]
# alert=0
# for j in range(12):
#     n=0
#     for i in range(1,len(wt)):
#         n+=int(l[wt[i]][j])
#     mon.append(n)
# for i in range(12,120):
#     n=mon[(i-12)]
#     n=int(n*1.01)
#     mon.append(n)
#     if alert==0 and n>160000:
#         print(str(i%12)+"."+str(int(2020+(i/12-i%12))))
#         alert=1
# plt.plot(mon)                                  
# plt.show()  

# 5.5
mon=[]
alert=0
for j in range(12):
    n=0
    for i in range(1,len(wt)):
        n+=int(l[wt[i]][j])
    mon.append(n)
for i in range(12,120):
    n=mon[(i-12)]
    n=int(n*1.01)
    mon.append(n)
    if alert==0 and n>(160000+1000*(i/12-i%12)):
        print(str(i%12)+"."+str(int(2020+(i/12-i%12))))
        alert=1

