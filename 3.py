# print('x y z w')
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             for w in 0,1:
#                 if ((x and w) or (w and z))==((z<=y)and(y<=x)):
#                     print(x,y,z,w)


from itertools import *
from math import prod
from pickle import FALSE


# for i in range(1,155):
#     z=bin(i)[2:]
#     n=z.count("1")
#     b=n%2
#     z=z+str(b)

#     n=z.count("1")
#     b=n%2
#     z=z+str(b)
#     if int(z,2)>97:
#         print(int(z,2))
    


# n=1
# s=0
# while n<=650:
#     s+=20
#     n*=5
# print(s)



# k=0
# for i in product('света',repeat=5):
#     if i.count("с")<1: continue
#     k+=1
#     print(k)




# d=49**7+7**20-28
# k=0
# while d>0:
#     if d%7==6:
#         k+=1
#     d=d//7
# print(k)



# M=0
# for x in range(1,100000):
#     for y in range(1,100000):
#         for a in range(1,100000):
#             if ((x>a)or(y>x)or((2*y+x)<110))==1:
#                 if a>M:
#                     M=a
#                 print(M)
            



# def f(n):
#     if n==1: return 1
#     if n>1: return 2 * g(n-1) + 5 * n
# def g(n):
#     if n==1: return 1
#     if n>1: return f(n-1) + 2 * n
# print(f(4)+g(4))

    
    

# def f(x,s):
#     if x>=31 and (s==2 or s==4): return True
#     if x>=31 and (s==3 or s==1): return False
#     if x<31 and s==4: return False
#     if x<31 and s<4:
#         if s%2==0:
#             return f(x+1,s+1) or f(x+2,s+1) or f(x*2,s+1)
#         else:
#             return f(x+1,s+1) and f(x+2,s+1) and f(x*2,s+1)
# for S in range(1,31):
#     if f(S,0)==True:
#         print(S)



# for n in range(1,1000):
#     x=n
#     a=0; b=0
#     while x > 0:
#         if x%2 > 0:
#             a += 1
#         else:
#             b += x%6
#         x = x//6
#     if a==2 and b==6:
#         print(n)


# def f(x,y):
#     if x>y: return 0
#     if x==y: return 1
#     return f(x+1,y)+f(x*2,y)+f(x*3,y)

# print(f(2,14)*f(14,28))



for x in range(35_000_000,40_000_000+1):
    k=0
    for y in range(1,int(x**0.5)+1):
        if x%y==0 and y%2!=0:
            k+=1
        if k>5:
            break
    if k==5:
        print(x)
