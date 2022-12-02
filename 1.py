# print("x y z w")
# for x in 0,1:
#     for y in 0,1:
#         for w in 0,1:
#             for z in 0,1:
#                 if (((x<=y)==(y<=z)) and (y or w)):
#                     print(x,y,z,w)

# s = 2
# k = 2
# while s < 50:
#     s += k
#     k += 2
# print(k)



# for n in range (1,1000):
#     x=n
#     l=0
#     m=1
#     while x > 0:
#         l += 1
#         if x%2 > 0:
#             m *= x%8
#         x = x//8
#     if m==25 and l==3:
#         print(n,m, l)



for j in range(210235, 210301):
   count = []
   for i in range(2, j // 2 + 1):
       if j % i == 0:
           count.append(i)
           if len(count) > 4:
               break
   if len(count) == 4:
       print(count)

        