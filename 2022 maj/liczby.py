import random
import os

mypath=os.getcwd()
mypath+="\\matury\\"
mypath+="2022 maj\liczby.txt"
print(mypath)
f=open(mypath,'w')
for i in range (200):
    r=random.randint(10,100000)
    f.write(str(r)+"\n")
f.close
