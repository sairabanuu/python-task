# num=int(input("enter a no:"))
# power=len(str(num))
# total=sum(int(digit)**power for digit in str(num))
# if total==num:
#     print("Armstrong number")
# else:
#     print("not arnstrong number")
    
#     #--------------or--------------
    
# def is_armstrong(num):
#     power=len(str(num))
#     total=sum(int(digit)**power for digit in str(num))
#     return total==num
# print(is_armstrong(153))
# print(is_armstrong(123)) 

# without using string
# num1=int(input("enter a no"))
# temp=num1
# count=len(str(temp))
# sum=0
# while temp>0:
#     digit=temp%10
#     sum+=digit**count
#     temp=temp//10
# if sum==num1:
#         print("arms")   
# else:
#         print("no")

# m=int(input("enter a no:"))
# n=int(input("enter ano:"))
# for  i in range(m,n+1):
         
#         num=str(i)
#         power=len(num)
#         total=sum(int(digit)**power for digit in num)
#         if total==i:    
#           print(i,end=" ")
    
num=int(input("enter a no:"))
num1=int(input("enter a no:"))

for i in range(num,num1+1):
    n=str(i)
    power=len((n))
    total=sum(int(digit)**power for digit in str(n))
    if total==i:
     print(i)
    # else:  
    #    print('no')
