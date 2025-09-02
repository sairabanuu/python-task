# method 1 factors of prime
# num=int(input('enter a no:'))
# # num=int(input('enter a no:'))
# count=0
# for i in range(1,num+1):
#     if num%i==0:
#         count+=1
# if count==2:
#     print(i)
# else:
#     print('not')

# # method 2
# num1=int(input('enter a no'))
# if num1<=1:
#     print('not a prime')
# else:
#     flag=True
#     for i in range(2,num1+1):
#         if num1%i==0:
#             flag=False
#             print('not a prime')
#             break
#     if flag==True:
#         print('prime')

# in function write this pgm
# def check_prime(in_num):
#     if in_num<=1:
#         return 'not a prime num'
#     for i in range(2,in_num):
#         if in_num%i==0:
#             return 'not a prime'
#     return 'prime'      
# print(check_prime(23))  

# method3
# def check_prime(in_num):
#     if in_num<=1:
#         return 'not a prime num'
#     for i in range(2,in_num//2+1):
#         if in_num%i==0:
#             return 'not a prime'
#     return 'prime'      
# print(check_prime(24)) 

# prime numbers     in given range
for i in range(2,51):
    flag=True
    for j in range(2,int(i**0.5)+1):
        
        if i%j==0:
            flag=False
            break
    if flag:
        print(i)
     
     
# def prime():
#     for i in range():
# def check_prime(num):
#     for i in range(2,50):
#      if num<=1:
#         return 'not a prime num'
#      for j in range(2,i):
#         if i%j==0:
#             break
#         print(i)
#         return 'not a prime'
#     return 'prime'      
# check_prime(11)