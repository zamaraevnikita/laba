# print("x y z w")
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             for w in 0,1:
#                 if(((x<=y)and (y<=w))or(z==(x or y)))==0:
#                     print(x,y,z,w)




# s=80
# n=0
# while s+n<150:
#     s=s-5
#     n=n+15
# print(n)



# for x in range(174457,174505+1):
#     d=[]
#     for y in range(2,x//2+1):
#         if x%y==0:
#             d.append(y)
#         if len(d)>2:
#             break
#     if len(d)==2:
#         print(d)




# x = int(input())
# a=0; b=10
# while x > 0:
#     d = x % 6
#     if d > a: a = d
#     if d < b: b = d
# x = x // 6
# print(a+b)
 


# def F(x,s,phod):
#     if x>=70 and s==2: return True
#     if x<70 and s==2: return False
#     if x>=70 and s==1: return False
#     if x<70 and s<2: return F(x+1,s+1,1) or F(x+4,s+1,2) or F(x*5,s+1,3)


# for S in range (1,69):
#     if F(S,0,0):
#         print (S)




# def F(x,s,phod):
#     if x>=70 and (s==1 or s==3): return True
#     if x<70 and s==3: return False
#     if x>=70 and s==2: return False
#     if x<70 and s<3:
#         if s==0:
#             return F(x+1,s+1,1) and F(x+4,s+1,2) and F(x*5,s+1,3)
#         elif s==1:
#             if phod==1: return F(x+4,s,2) or F(x*5,s+1,3)
#             if phod==2: return F(x+1,s,1) or F(x*5,s+1,3)
#             if phod==3: return F(x+1,s,1) or F(x+4,s+1,2)

# for S in range (1,69):
#     if F(S,0,0):
#         print (S)


# def F(x,s,phod):
#     if x>=70 and (s==2 or s==4): return True
#     if x<70 and s==4: return False
#     if x>=70 and (s==1 or s==3): return False
#     if x<70 and s<4:
#         if s==0:
#             return F(x+1,s+1,1) and F(x+4,s+1,2) and F(x*5,s+1,3)
#         elif s==2:
#             if phod==1: return F(x+4,s+1,2) and F(x*5,s+1,3)
#             if phod==2: return F(x+1,s+1,1) and F(x*5,s+1,3)
#             if phod==3: return F(x+1,s+1,1) and F(x+4,s+1,2)

#         elif s==1 or s==3:
#             if phod==1: return F(x+4,s+1,2) or F(x*5,s+1,3)
#             if phod==2: return F(x+1,s+1,1) or F(x*5,s+1,3)
#             if phod==3: return F(x+1,s+1,1) or F(x+4,s+1,2)


# for S in range (1,69):
#     if F(S,0,0):
#         print (S)






#1вариант решения
# f=open('k7.txt')
# s=f.readline()
# s=s.replace('XYZ','*')
# s=s.replace('X',' ')
# s=s.replace('Y',' ')
# s=s.replace('Z',' ')
# m=s.split()
# M=0
# for el in m:
#     M=max(M,len(el))
# print(M)




#2вариант решения
# f=open('k7.txt')
# s=f.readline()
# k=0
# m=0
# for el in s:
#     if (el=='X' and k%3==0) or (el=='Y' and k%3==1) or (el=='Z' and k%3==2):
#         k+=1
#         m=max(k,m)
#     else:
#         k=0
# print(m)
