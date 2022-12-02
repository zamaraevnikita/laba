# 1:	20	
# 2:	wzyx	
# 3:	38349	
# 4:	20
# 5:	256	
# 6:	30	
# 7:	256	
# 8:	159
# 10:	245	
# 11:	2175	
# 12:	5533
# 13:	12	
# 14:	478	
# 15:	0	
# 16:	448
	
# 19:   6
# 20:   14 22
# 21:	21
# 22:	140	
# 23:	52	
# 24:	110


from itertools import *






# # print("x y z w")
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             for w in 0,1:
#                 if(((z<=y)and((not(x))<=w))<=((x==w)or(y and (not(x)))))==0:
#                     print(x,y,z,w)




# for x in range(1,300):
#     z=bin(x)[2:]
#     e=z.count('1')
#     if x%2==0: z=z+bin(e)[2:]
#     else: z='1'+z+'00'
#     if (int(z,2)<1000):
#         print(x)


# k=0
# for x in range(1,1000):
#     s = 6 * (x // 5)
#     n = 1
#     while s < 300:
#         s = s + 35
#         n = n * 2
#     if n==64:
#         k+=1
#     print(k)



# f=open('24-200.txt')
# k=0
# for i in f:
#     x=i.replace("\n",'').split('.')
#     if x[0]=='195' and x[1][0]=='2' and len(x[1])==2 and len(x[2])==3 and \
#         x[2][0]=='1' and x[2][-1]=='5' and x[3]=='14':
                    
#         k+=1
# print(k)



# def f(x,y):
#     if x==y: return 1
#     if x>y: return 0
#     return f(x+1,y)+f(x*2,y)+f(x*3,y)
# print(f(2,7)*f(7,28))






# 1
# def F(x,y,s):
#     if x+y>=95 and s==2: return True
#     if x+y<95 and s==2:return False
#     if x+y>=95 and s<2: return False
#     if x+y<95 and s<2:
#         return F(x+1,y,s+1) or F(x,y+1,s+1) or F(x*4,y,s+1) or F(x,y*4,s+1)
# for S in range (1,89):
#     if F(5,S,0)==True:
#         print(S)



# def F(x,y,s):
#     if x+y>=95 and s==3: return True
#     if x+y<95 and s==3:return False
#     if x+y>=95 and s<3: return False
#     if x+y<95 and s<3:
#         if s%2==1:
#             return F(x+1,y,s+1) and F(x,y+1,s+1) and F(x*4,y,s+1) and F(x,y*4,s+1)
#         else:
#             return F(x+1,y,s+1)or F(x,y+1,s+1) or F(x*4,y,s+1) or F(x,y*4,s+1)


# for S in range (1,89):
#     if F(5,S,0)==True:
#         print(S)




# def F(x,y,s):
#     if x+y>=95 and (s==2 or s==4): return True
#     if x+y<95 and s==4: return False
#     if x+y>=95 and (s==3 or s==1): return False
#     if x+y<95 and s<4:
#         if s%2==0:
#             return F(x+1,y,s+1) and F(x,y+1,s+1) and F(x*4,y,s+1) and F(x,y*4,s+1)
#         else:
#             return F(x+1,y,s+1)or F(x,y+1,s+1) or F(x*4,y,s+1) or F(x,y*4,s+1)


# for S in range (1,89):
#     if F(5,S,0)==True:
#         print(S)

# def f(n):
#     if n==1: return 1
#     if n>=2 and n%2==0: return f(n/2) + 1
#     if n>=2 and n%2!=0: return f(n-1) + n
# for x in range(1,1000):
#     if f(x)==19:
#         print(x)




# x=53**123+65**2222-172**12
# n=''
# while x>0:
#     n=str(x%7)+n
#     x=x//7
# print(n)





# f=open('17-292.txt')
# k=0
# a=[]
# M=0
# for i in f:
#     a.append(int(i))
# for i in range(len(a)-1):
#     if (a[i]%6+a[i+1]%6) == (a[i]%11+a[i+1]%11):
#         k+=1
#         M=max(M,a[i]+a[i+1])
# print(k,M)


# def f(x):
#     if x<=1: return False
#     for i in range(2,int(x**0.5)+1):
#         if x%i==0: return False
#     return True
# n=[]
# for x in range(3850000,5000000+1):
#     d=[]
#     for i in range(1,int(x**0.5)+1):
#         if x%i==0:
#             if f(i):d.append(i)
#             if f(x//i): d.append(x//i)
#     d.sort()
#     z=max(d)
#     s =''
#     for el in d:
#         s+=str(el)
#     if s[0]=='2' and s[1]=='7' and s[-1]=="1" and s[-3]=="1":
        
#         print(x,z)



# n=[]
# for x in range(159,10**9):
#     d=[]
#     for i in range(1,int(x**0.5)+1):
#         if x%i==0:
#             if f(i):d.append(i)
#             if f(x//i): d.append(x//i)
#     d.sort()
#     z=max(d)
#     s =''
#     for el in d:
#         s+=str(el)
#     if s[0]=='2' and s[1]=='7' and s[-1]=="1" and s[-3]=="1":
        
#         print(x,z)
# a=[]
# for x in range(5):
#     for i in product('234678',repeat=x):
#         s=''.join(i)
#         a.append(s)
# res=[]
# for x in a:
#     for y in a:
#         s="1"+x+"5"+y+"9"
#         for n in range(len(s)-1):
#             if s[n]>=s[n+1]: break
        
#         else:
#             if int(s)<10**9 and int(s)%21==0:
#                 res.append([int(s),int(s)//21])
# res.sort()
# print(res)


# def f(x):
#     if x<=1: return False
#     for i in range(2,int(x**0.5)+1):
#         if x%i==0: return False
#     return True

# n=[]
# for x in range(4679000,7000000+1):
#     d=[]
#     for i in range(1,int(x**0.5)+1):
#         if x%i==0:
#             if f(i):d.append(i)
#             if f(x//i): d.append(x//i)
#     d.sort()
#     s =''
#     for el in d:
#         s+=str(el)
#     if (s[0]=='2' and s[1]=='7' and s[-2]=="9" and s[-3]=='3') or (s[0]=='3' and s[1]=="4" and s[-1]=="7" and s[-3]=="2"):
        
#         print(x,max(d))



# def f (x):
#     if x<=1: return False
#     for i in range(2,int(x**0.5)+1):
#         if x%i==0: return False
#     return True

# for x in range(2352000,5000000):
#     delit=[]
    
#     for i in range(1,int(x**0.5)+1):
#         if x%i==0:
#             if f(i):delit.append(i)
#             if f(x//i): delit.append(x//i)
#     delit.sort()
#     s =''
#     for el in delit:
#         s+=str(el)
#     if s[0]=='1' and s[1]=='0' and s[-1]=="9" and s[-2]=='2':
        
#         print(x,max(delit))



# a=[]
# for x in '0123456789':
        
#         a.append(x)
# res=[]
# for x in a:
#     for y in a:
#         s="12345"+x+'6'+y+'8'      
#         if int(s)<10**9 and int(s)%17==0:

#             res.append([int(s),int(s)//17])
# res.sort()
# print(res)



# res=[]
# for x in range(123405,1000000):
#     delit=[]
    
#     if x%148==0:
#         delit.append(x%148)
        
#     delit.sort()
#     s =''
#     for el in delit:
#         s+=str(el)
#     if s[0]=='1' and s[1]=='2' and s[2]=="3" and s[-1]=='5' and s[-3]=="4":
#         n=''
#         while x>0:
#             n=str(x%3)+n
#             x=x//3
# res=[]
# for z in '012':
#     for y in '012':
#         for k in '012':
#             for m in '012':
#                 for j in '012':
#                     s='2'+z+'1'+y+'2'+k+'1'+m+"2"+j+'1'
#                     if int(s,3)%148==0:

#                                 res.append([int(s,3),int(s,3)//148])
# res.sort()
# print(res)
                        



# x=31
# y=''
# while x>0:
#     y=str(x%5)+y
#     x=x//5
# print(y)


# def f(x):
#     if x>36: return 0
#     if x==36: return 1
#     return f(x+1)+f(x+10)
# print(f(15))


# a=[]
# k=0
# for i in product('стол',repeat=4):
#     s=''.join(i)
#     a.append(s)
#     if s.count('о')>1: continue
#     else: k+=1
# print (k)


# res=[]
# for x in a:
#     for y in a:
#         s="1"+x+"5"+y+"9"
#         for n in range(len(s)-1):
#             if s[n]>=s[n+1]: break
        
#         else:
#             if int(s)<10**9 and int(s)%21==0:
#                 res.append([int(s),int(s)//21])
# res.sort()
# print(res)







# res=[]
# for z in '0123456789abcdef':
#     for y in '0123456789abcdef':
        
#         s='1'+z+'ded'+y+'baba'
#         if int(s,16)%186==0:
#             res.append([int(s,16),int(s,16)//186])
# res.sort()
# print(res)



# res=[]
# for z in '01':
#     for y in '01':
#         for k in '01':
#             for m in '01':
#                 for j in '01':
#                     for g in '01':
#                         s='1'+z+'1'+y+'1'+k+'1'+m+"1"+j+g+'1'
#                         if int(s,2)%45==0:

#                                 res.append([int(s,2),int(s,2)//45])
# res.sort()
# print(res) 






# res=[]
# for z in '01234567':
#     for y in '01234567':
        
#         s='1'+z+'345'+y+'700'
#         if int(s,8)%76==0:
#             res.append([int(s,8),int(s,8)//76])
# res.sort()
# print(res)


# def f(x):
#     if x<=1: return False
#     for i in range(2,int(x**0.5)+1):
#         if x%i==0: return False
#     return True
# for x in range(2022,200,-1):
#     d=[]
#     for i in range(1,int(x**0.5)+1):
#         if x%i==0:
#             if f(i):d.append(i)
#             if f(x//i): d.append(x//i)
#     d.sort()
#     z=min(d)
#     if z>10 and x!=z:
#         print(x,z)


# def f(x):
#     if x<=1: return False
#     for i in range(2,int(x**0.5)+1):
#         if x%i==0: return False
#     return True
# def g(n):
#     f=1
#     for i in range(1,n+1):
#         f*=i
#     return f

# for i in range(14,1,-1):
#     z=g(i)
#     d=[]
#     for j in range(1,int(z**0.5)+1):
#         if z%j==0:
#             if f(j):d.append(j)
#             if z//j!=j and f(z//j):d.append(d//j)
#     if len(d)%2==1:
#         print(i,len(d))

    



def s(x):
    summ=0
    while x > 0:
        d = x % 10
        summ += d
        x //= 10
    return summ
def f(x):
    if x<=1: return False
    i=1
    while i*i<=z:
        if x%i==0: return False
        i+=1
    return True
def g(x):
    f=1
    for i in range(1,x+1):
        f*=i
    return f

for i in range(2022,22,-1):
    print(i)
    z=g(i)
    d=[]
    j=1
    while j*j<=z:
        
        if z%j==0:
            if f(j):d.append(j)
            if z//j!=j and f(z//j):d.append(z//j)
        j+=1
    if len(d)%2==1 and s(i)%22==0:
        print(i,len(d))

    