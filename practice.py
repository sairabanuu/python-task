# i=1
# while i <=10:
#     print("7 *",i,"=",7*i)
#     i+=1

# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
    
# n=int(input('enter a num:'))
# for i in range(1,n+1):
#     print('*'*i)
#     i+=1

# n=int(input('enter a no:'))
# s=65
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(chr(s),end=" ")
#     s+=1 
#     print()    
#     i+=1

# num=int(input('enter a no:'))
# if num%2==0:
#     print(num,'even')
# else:
#     print('odd')

# num1=int(input('enter a no:'))
# num2=int(input('enter a no:'))
# if num1>num2:
#     print(num1)
# else:
#     print(num2)


# num1=int(input('enter a no1:'))
# num2=int(input('enter a no2:'))
# num3=int(input('enter a no3:'))
# if num1>num2>num3:
#     print(num1)
# elif num1<num3:
#     print(num3)
# else:
#     print(num2)

# n=int(input('enter a no:'))
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print(sum)

# n=int(input('enter a no:'))
# for i in range(1,n+1):
#     if i%2==0:
#         print(i)
    
# num=int(input('enter a no:'))
# for i in range(1,num+1):
#     for j in range(1,11):
#        print(i,'*',j,'=',i*j)

# i=1
# count=0
# while(i<=10):
#    count+=1
#    print(i)
#    i+=1
# print(count)

# num=1234
# sum=0
# while num<=10:
#     sum+=num
# print(sum)

# num=123
# sum=0
# while(num!=0):
#    rem=num%10
#    sum+=rem
#    num//=10
# print("sum:",sum)

# for i in range(0,4):
#    pass_word=(input("enter a password"))
#    if pass_word=="12345":
#      print("Login Successful")
# else:
#      print("Accont locked")

# number=(input("enter a number"))
# for i in number:
#     digit=int(i)
#     if digit!=0: 
#         print(digit)
#     else:
#         break
    
# for i in range(1,21):
#     if i%3==0:
#      continue
#     print(i)
    
# while True:
#   num1=int(input("enter a number:"))
#   if num1==0:
#      break
#   else:
#      print(num1)

# even_count=0
# odd_count=0
# for i in range(5):
#   num1=int(input("enter a number:"))
#   if num1%2==0:
#      even_count+=1
#   else:
#      odd_count+=1
# print("even numbers:",even_count)
# print("odd numbers:",odd_count)

# str1=input("enter a string:")
# for i in str1:
#    print(i)

# num1=int(input("enter a number:"))
# if num1%2==0 and num1%5==0:
#   print(num1,"is divisible by 2 and 5:")
# elif num1%2==0:
#   print(num1,"is divisible by 2 not by 5 ")
# else:
#   print(num1,"is not divisible by both 2 and 5")

# num1,num2,num3=32,4,5
# if num1>num2 and num1>num3:
#   print(num1)
# elif num2>num3:
#   print(num2)

# def leap(year):
#   return 'leap year'if (year %400==0) or (year % 100 !=0 and year % 4==0) else 'not leap year'
# num=int(input('enter ano:'))
# print(leap(num))

# def triangle(s1,s2,s3):
#  if s1+s2>s3 and s1+s3>s2 and s2+s3>s1:
  
#   if s1==s2 and s2==s3:
#        print('triangle is equilatral')
#   elif s1==s2 or s2==s3 or s1==s3:
#         print('triangle is isosceles')
#   else:
#          print('triangle is scalene')
# triangle(3,4,5)
  
  
  


# input_char=input('enter a char')
# def vowels(char):
#   if len(char)!=1:
#     return 'invalid'
#   if char in 'AEIOUaeiou':
#     print('vowels')
#   else:
#     print('consonant')
# # input_char=input('enter a char')
# # print(vowels(input))
# vowels(input_char)

# def sum(n1,n2):
#   print(n1+n2)
# sum(2,3)

# def product(n1):
#   print(n1**2)
# product(3)


# start=1
# while start<100:
#       if start%2==0:
#             print(start)
#       start+=1
#  another method by using while loop
# start=2
# while start<100:
#    print(start)
#    start+=2

# sum of natural numbers
# n=57
# sum=0
# for i in range(1,n+1):
#       sum=sum+i
# print(sum)
# by using while loop
# n=1
# sum=0
# while n<=1:
#     sum+=n
# print(sum)

# n=int(input('enter a num:'))
# for i in range(n,n+1):
#       if n==-n:
#             print(n,'negative num')
#       else:
#             print(n)

# while True:
#       ip_num=float(input('enter a num'))
#       if ip_num<=0:
#             print('negative')
#             break
      # or
# ip_num=float(input('enter a no:'))
# while ip_num>0:
#       print('nrgative') 
#      or
# ip_num=float(input('enter a num'))
# if ip_num<=0:
#       print('negative')
# while ip_num>0:
#       ip_num=float(input('enter a positive number'))
#       if ip_num<=0:
#             print('negative')
     
            

# num=17
# if num%2==0 and  num%3==0 and num%6==0:
#       print(num,'satisfy')
# else:
      # print('not satisfy')
      
# num=int(input('enter a no:'))
# if num%2==0:
#       print(num,'even number')
# else:
#       print(num,'odd number')

# num1=int(input('enter a no:'))
# if num1%5==0 and num1%10!=0:
#       print(num1,'divisible by 5')
# else:
#       print('invalid')

# num1=int(input('enter a no:'))
# num2=int(input('enter a no:'))
# if num1>num2:
#       print(num1)
# else:
#       print(num2)

# num1=int(input('enter a no:'))
# num2=int(input('enter a no:'))
# if num1<num2:
#       print(num1)
# else:
#       print(num2)

# num=12
# if num%2==0 and num%3==0 and num%6==0:
#       print(num,'satisfy')
# else:
#       print('not satisfy')

# num=int(input('enter a no:'))
# if num>=18:
#       print('eligible')
# else:
#       print('not eligible')


# sub1=45
# sub2=40
# sub3=30
# if sub1>=35 and sub2>=35 and sub3>=35:
#       print('pass')
# else:
#       print('fail')

# sub1=35
# sub2=30
# sub3=30
# if sub1>=35 or sub2>=35 or sub3>=35:
#       print('pass')
# else:
#       print('fail')

# sub1=35
# sub2=35
# sub3=30
# if sub1>=35 and sub2>=35 or sub3>=35:
#       print('pass')
# else:
#       print('fail')

# n1,n2,n3=3,4,6
# if n1>n2 and n1>n3:
#       print(n1)
# elif n2>n3:
#       print(n2)
# else:
#       print(n3)
      
# n1,n2,n3=3,4,6
# if n1<n2 and n1<n3:
#       print(n1)
# elif n2<n3:
#       print(n2)
# else:
#       print(n3)

# num=int(input('enter a no:'))
# if num**num:
#       print('perfect square')
# else:
#       print('not')

# n1,n2,n3=3,4,6
# if n1>n2:
#       print(n1)
# elif n2<n3:
#       print(n2)
# else:
#       print(n3)
      
# year=int(input('enter a no:'))
# if (year%400==0) or (year%4==0 and year %100!=0):
#       print('leap year')
# else:
#       print('not leap year')

# n=int(input('enter a n0:'))
# for i in range(1,n+1):
#       print(i)
      
# m=7
# for i in range(3,m+1):
#       print(i)
        
# n=int(input('enter a n0:'))
# for i in range(n, 0, -1):
#      print(i)

# n=int(input('enter a n0:'))
# n1=int(input('enter a no:'))
# while n>=n1:
#       # for j in range(n,0,n1):
#   print(n)
#   n-=1

# n=int(input('enter a no:'))
# sum=0
# for i in range(1,n+1):
#       sum+=i
# print(sum)

# n=int(input('enter a no:'))
# factor=16
# for i in range(1,n+1):
#       factor*=i
# print(factor)

# n=3
# m=6
# sum=0
# for i in range(n,m+1):
#       sum+=i     i
# print(sum) 

# n=2
# m=6
# product=1
# for i in range(n,m+1):
#       product*=i
# print(product)

# n=10
# count=0
# for i in range(1,n+1):
#       if n%i==0:
#          count+=1
# print(count)

# n=8
# for i in range(n,n+1):
#       if i%2!=0:
#             print('prime')
#       else:
#             print('even')
            
# n=3
# m=8
# for i in range(n,m+1):
#       if i%2==0:
#             print(i)

# n=3
# m=8
# for i in range(n,m+1):
#       if i%2!=0:
#             print(i)

# n=3
# m=8
# even_count=0
# odd_count=0
# for i in range(n,m+1):
#       if i%2==0:
#             even_count+=i
#       else:
#             odd_count+=i
#       print('even',even_count,'odd',odd_count)


# db_username='saira'
# db_password=12345
# remaining_attempts=3
# while remaining_attempts>0:
#       input_username=input('enter username')
#       input_password=input('enter password')
#       if input_username==db_username and input_password==db_password:
#             print('login done')
#             print('redirecting')
#       else:
#             remaining_attempts-=1
#             print('login failed')


# num=12345
# print(len(str(num)))
# str1=str(num)
# sum=0
# for i in str1:
#       sum+=int(i)
# print(sum)
# another mthod
# num1=2456
# count=0
# sum=0
# while num1>0:
#       rem=num1%10
#       print(rem)
#       que=num1//10
#       num1=que
#       count+=1
#       sum+=rem
#         # num1=num1//10
# print(count)
# print(sum)

# problem solving ques
# str='madam'
# if str==str[::-1]:
#       print('palindrome')
# else:
#       print('not')

# sum of digits
# num=1234
# print(len(str(num)))
# str1=str(num)
# sum=0
# for i in str1:
#       sum+=int(i)
# print(sum)

# product of digits
# num=1234
# print(len(str(num)))
# str1=str(num)
# sum=1
# for i in str1:
#       sum*=int(i)
# print(sum) 


# num=int(input('enter a no:'))
# order=len(str(num))
# sum_of_powers=0
# while num>0:
#       num1=num%10
#       sum_of_powers+=num1**order
# if sum_of_powers==num:
#       print('armstrong')
# else:
#       print('not') 


# str1='saira'
# print(str1[::-1])
# or
# str1='banu'
# if str1==str1[::-1]:
#       print(str1)
# else:
#       print('not')


            

# n=50
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count+=1
#         print(i)    
# if count==2:
#     print(count)



# for i in range(1,50):
#       if i%2==0:
#         print(i)    

# l1=[2,3,4,6,9,11,15,25,35,40]
# for i in l1:
#   if i>=10: 
#     print(i) 


# s1,s2,s3=3,4,5
# if s1+s2>s3 and s1+s3>s2 and s2+s3>s1:
#        print('triangle')
# else:
#       print('not')
      
# num=50
# for i in range(1,num+1):
#       if num%i==0:
#             print(i)

# num=50
# count=0
# for i in range(1,num+1):
#     if num%i==0:
#         count+=1
# if count==2:
#     print('prime')
# else:
#     print('not')
    
# for num in range(2,101):
#       flag=True
#       for i in range(2,int(num**0.5)+1):
#             if num%i==0:
#                   flag=False
#                   break
#       if flag:
#                   print(num,end=" ")
                  
     
# def prime_number(m,n):
#       for i in range(m,n+1):
#             count=0
#             for j in range(2,int(i**0.5)+1):
#                   if i%j==0:
#                         count+=1
#                         break
#                   if count==0:
#                         print(i)
# prime_number(2,51)
 
# Armstrong number
# num=int(input('enter a no:'))
# order=len(str(num))
# if sum(int(digit)**order for digit in str(num))==num:
#       print(num)
# else:
#       print('no')
      
# num=153
# for i in str(num):

# num=28
# product=0
# for i in range(1,num):
#   if num%i==0:
#       product+=i
# if product==num:
#       print(num,'perfect')
# else:
      # print('no')  
      
# num=36
# num1=num**0.5
# if num1==int(num1):
#       print(num,'p square') 
# else:
#       print('no')   
      

            

# num=int(input('enter a num:'))
# num2=int(input('enter a nun:'))
# prime_count=0
# composite_count=0
# for i in range(num,num2+1):
#     if i>1:
#         is_prime=True
#         for j in range(2,int(i**0.5)+1):
#             if i%j==0:
#                 is_prime=False
#                 break
#             if is_prime:
#                 prime_count+=1
#             else:
#                 composite_count+=1
# print(prime_count) 
# print(composite_count)-

n1=2451
# temp=n1
# rev=0
sum=0
while n1>0:
    digit=n1%10
    if digit%2==0:
        print(digit)
    n1=n1//10