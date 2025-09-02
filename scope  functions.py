# global scope-3rd priority
# local scpe-1st priority
# enclosed scope-2nd priority
# built in scope-4th priority


# global scope-out side of the function we cab accsess any where
# num=2-global scope
# def check_scope():
    # num=3-enclosed scope
    # def second():-nested function means function in function
        # num=4-localscope
        # print(num)-1st print local scope
    # second() -we call this function inside the first function  
    # print(num)-2nd print enclosed scope
# check_scope()
# print(num)-global scope last print

# num=3
# def first():

#     global num
#     num=5
#     print(num)
# first()

# num=5
# def first():
    # num=9
    # globals ()['num']=3-global function we can re assign value
    # print(num)
# first()
# print(num)
   

# def is_prime(n):
#     if n<2:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True
# print(is_prime(11))
    
    
# def lcm(a,b):
#     def gcd(x,y):
#         while y:
#             x,y=y,x%y
#         return x
#     return (a*b)
# print(lcm(4,6))

# import calendar
# year,month,date=2025,6,5
# print(calendar.month(year,month,date))

# for i in range(1,50):
#     flag=True
#     for j in range(2,int((i**0.5)+1)):
#         if i%j==0:
#             flag=False
#     if flag:
#          print(i)

# n=7
# for i in range(1,11):
#     print(n,"*",i,'=',n*i)
     