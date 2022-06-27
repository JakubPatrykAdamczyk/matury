import os

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
# 5.2
dziel={}
print(wt[1][7:10])
for i in range(1,len(wt)):
    dziel[wt[i][7:10]]=0
for i in range(1,len(wt)):
    n=0
    for j in range(12):
        n+=int(l[wt[i]][j])
    n+=dziel[wt[i][7:10]]
    dziel[wt[i][7:10]]=n
print(dziel)