
# 5.3
dziel={}
print(wt[1][7:10])
for i in range(1,len(wt)):
    dziel[wt[i][7:10]]=0
for i in range(1,len(wt)):
    t=[]
    for j in range(12):
        n=0
        n+=int(l[wt[i]][j])
        n+=dziel[wt[i][7:10]]
        t.append(n)
    
    dziel[wt[i][7:10]]=t
    del t
print(dziel)