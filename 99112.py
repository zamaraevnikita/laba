from itertools import *
# print("x y z w")
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             for w in 0,1:
#                 if(((w<=z)and((not(x))<=y))<=((y==w)or(z and (not(x)))))==0:
#                     print(x,y,z,w)






a=[]
for x in range(169,10**9):
    
    s=''.join(str(x))
    a.append(s)
res=[]
for x in a:
    for y in a:
        s="123"+x+"4"+y+"5"
        for n in range(len(s)-1):

            if int(s)<10**9 and int(s)%169==0 and len(s[-2])==1:
                res.append([int(s),int(s)//169])
res.sort()
print(res)