import os

mypath=os.getcwd()
mypath+="\\matury\\"
mypath+="2022 maj\zad4\liczby.txt"
f=open(mypath)
t=[]
for i in f:
    t.append(int(i))

# #4.1
# a1=0
# a_num=0

# for i in range(len(t)):
#     a=str(int(t[i]))
    
#     if len(t[i])>2:
#         if a[0]==a[-1]:
#             a_num+=1
#             if a1==0:
#                 print(t[i])
#                 a1=1
#     if len(t[i])>4:
#         if a[0:2]==(a[-2]+a[-1]):
#             a_num+=1
#             if a1==0:
#                 print(t[i])
#                 a1=1
# print(a_num)


# #4.2
# l={}
# i_max1=0
# i_max2=0
# i_vmax1=0
# i_vmax2=0
# for i in range(len(t)):
#     a=int(t[i])
#     z=2
#     z_o=0
#     f=""
#     imaxn1=0
#     imaxn2=0
#     while a!=1:
#         if a%z==0:
#             f+=str(z)+" "
#             a=a/z
#             imaxn1+=1
#             if z_o==z:
#                 imaxn2+=1
#                 z_o=z
#         else: z+=1
#     if i_vmax1<imaxn1:
#         i_vmax1=imaxn1
#         i_max1=i
#     if i_vmax2<imaxn2:
#         i_vmax2=imaxn2
#         i_max2=i
#     l[str(t[i])]=f
# # print(l)
# print(str(t[i_max1])+" : "+l[str(t[i_max1])])
# print(str(t[i_max2])+" : "+l[str(t[i_max2])])
        
# 4.3
t.sort()
print(t)
a3=0
a5=0
for i in range(len(t),0):
    av=1
    print(t[i])


  


