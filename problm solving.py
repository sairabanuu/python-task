# neon number
# num=int(input('enter a number:'))
# square=num*num
# # sum=0
# # while square>0:
# #     sum+=square%10
# #     square//=10
# sum=sum(int(digit) for digit in str(square))
# if sum==num:
#     print("neon")
# else:
#     print('not')

# fibonacci series
# n=10
# a,b=0,1
# # print('fibonacci series')
# for i in range(n):
#     print(a,end=" ")
#     a,b=b,a+b

# harshad number
# num=17
# sum=sum(int(digit) for digit in str(num))
# if num%sum==0:
#     print(num)
# else:
#     print('not')


# perfect number
# num=int(input('enter a no:'))
# sum=0
# for i in range(1,num):
#     if num%i==0:
#         sum+=i
# if sum==num:
#         print(num,'perfect')
# else:
#         print('no')

# count vowels and consonants
# str1='sairabanu'
# vowels='aeiou'
# vowel_count=0
# consonant_count=0
# for ch in str1:
#     if ch in vowels:
#         vowel_count+=1
#     else:
#         consonant_count+=1
# print('vowels:',vowel_count,'con:',consonant_count)      

# count consonants in string
# str1='satvika'
# vowels='aeiou'
# consonant_count=0
# for ch in str1:
#     if ch not in vowels:
#         consonant_count+=1
# print('consonant:',consonant_count)  


# count vowels in string
# str1='satvika'
# vowels='aeiou'
# vowels_count=0
# for ch in str1:
#     if ch  in vowels:
#         vowels_count+=1
# print('vowels:',vowels_count)  


# palindrome
# str='121'

# if str==str[::-1]:
#     print(str,'palindrome')
# else:
#     print('no')

# solid square pattern
# n=4
# for i in range(n):
#     for j in range(n):
#         print('*',end=" ")
#     print()
        
# solid rectangle pattern
# n,m=3,5
# for i in range(n):
#     for j in range(m):
#         print('*',end=" ")
#     print()


# right-angled triangle(left aligned)
# n=5
# for i in range(1,n+1):
#     for i in range(i):
#         print('*', end=" ")
#     print()


# inverted triangle(left aligned)
# n=5
# for i  in range(1,n+1):
#     for j in range(i,n+1):
#         print('*',end=" ")
#     print()

# centered pyramid pattern
# n=4
# for i in range(n):
#     # for j in range(i,n+1):
#         print(' ' * (n-i-1),end=" ")
#         print('*'*(i+1))

# sum of all digits
# num=101
# sum=sum(int(digit)for digit in str(num))
# print(sum)

# reverse a string or num
# num=765
# num1=str(num)
# print((num1[::-1]))

# num=3
# product=1
# # num1=str(num)
# for i in range(1,num+1):
#     product*=i
# print(product)
    
# str1='world'
# n=len(str1)
# mid=n//2
# if n%2==0:
#     print(str1[mid-1]+str1[mid])
# else:
#     print(str1[mid])

# print(str1[2:3])


# n=755547
# s=str(n)
# first=int(s[0])
# last=int(s[-1])
# sum=first+last
# middle_sum=0
# for digit in s[1:-1]:
#     middle_sum+=int(digit)
# if sum==middle_sum:
#     print('equal')
# else:
#     print('not equal')




# n=84719
# s=str(n)
# first=s[0]
# middle=s[1:4]
# last=s[-1]
# if first>middle and last>middle:
#     print('true')
# else:
#     print('false')

# s='helloworld'
# vowels='aeiou'
# for ch in s:
#     if ch in vowels:
    
#         # print(ch)
# s.reverse()

    # if flag=  / 


# m=1
# n=500
# for num in range(m,n+1):
#     digits=len(str(num))
#     total=0
#     temp=num
#     while temp>0:
#         digit = temp%10
#         total+=digit**digits
#         temp//=10
#     if total==num:
#         print(num,end=" ")


# last_prime=None
# for i in range(10,25):
#     flag=True
#     if i<2:
#         continue
#     for j in range(2,int(i**0.5)+1):
#         if i%j==0:
#             flag=False
#             break
#     if flag:
#         last_prime=i
#         # break
# print(last_prime)

# str1='krishna'
# vowels='aeiou'
# last_vowel=None
# for ch in str1:
#     if ch in vowels:
#        last_vowel=ch
#     #    break
# if last_vowel:
#     print(last_vowel)
# else:
#     print('no')
        
            
# for i in range(1,11):
#     if i%2!=0:
#             print(i)
#             continue

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
# print(composite_count)               

# armstrong
# def armstrong(num):
#     power=len(str(num))
#     total=sum(int(digit)**power for digit in str(num))
#     if total==num:
#         print("true")
#     else:
#         print("false")
# armstrong(153)

# def add(a,b):
#     print(a+b)
# add(2,3)

# def check_even_odd(n1):
#        if n1%2==0:
#            print("even")
#        else:
#            print("odd")
# check_even_odd(3)    
        
# def leap(num):
#     if (num%400==0) or (num%100!=0 and num%4==0):
#         print("leap year")
#     else:
#         print("no")
# leap(2026)

# n=100
# m=500
# for i in range(n,m+1):
#     power=len(str(i))
#     total=sum(int(digit)**power for digit in str(i))
#     if total==i:
#         print(i)

# def prime_num(n1):
#     for i in range(n1):
#         flag=True
#         if i%n1==0:
#             flag=False
#             break
#     if flag:
#         print(i)
# prime_num(11)
        
# fibonacci series
# num1,num2=0,1
# n=10
# for i in range(n):
#     third_num=num1+num2
#     print(num1)
#     num1=num2
#     num2=third_num

# l1=[4,5,7,6,3,10,9,54,64,34,25]
# l1.sort(reverse=True)
# print(l1)

# l2=[2,4,6,87,54,90]
# print(min(l2))

# l2=[2,4,6,87,54,90]
# l2.append(4)
# print(l2)

# s1="satvika"
# vowels="aeiou"
# for ch in s1:
#     if ch not in vowels:
#       print(ch,end="")

# l2=[2,4,6,87,54,90]-element delete
# l2.remove(6)
# print(l2)

# l2=[2,4,6,87,54,90]-index delete
# del l2[2]
# print(l2)

# hcf,lcm
# a,b=20,15
# hcf=1
# for i in range(1,min(a,b)+1):
#     if a%i==0 and b%i==0:
#         hcf=i
# lcm=(a*b)//hcf
# print(hcf)
# print(lcm)


# l2=[2,4,6,87,54,90,2,3,5,7,4]-remove duplicates
# _list=list(set(l2))
# print(_list)

# n1=2
# n2=4
# temp=n2
# n2=n1
# n1=temp
# or
# n1,n2=n2,n1
# print(n1,n2)

# n1=12116
# temp=n1
# reverse_no=0
# while n1>0:
#     digit=n1%10
#     reverse_no=reverse_no*10+digit
#     n1=n1//10
# print(reverse_no)
# if reverse_no==temp:
#     print('palindrome')

# n1=2451
# # temp=n1
# # rev=0
# sum=0
# while n1>0:
#     digit=n1%10
#     if digit%2==0:
#         print(digit)
#     n1=n1//10

# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(5))

# num=6
# fact=1
# for i in range(1,num+1):
#     fact*=i
# print(fact)
    
# num=10
# sum=0
# for i in range(1,num+1):
#     sum+=i
# print(sum)

# num=2
# if num%2==0:
#     print('even')
# else:
#     print('odd')

# l1=[1,3,45,6,7]
# l2=min(l1)
# print(l2)

# n1,n2,n3=4,5,6
# largest=max(n1,n2,n3)
# print(largest)

# num=1234
# sum=0
# while num>0:
#     digit=num%10
#     sum+=digit
#     num//=10
# print(sum)

# num=15
# fact=1
# for i in range(1,num+1):
#     fact*=i
# print(fact)

s1='hello'
rev=""
for ch in s1:
    rev=ch+rev
    print(rev)
# reversed_s1="".join(reversed(s1))
# print(reversed_s1)

# n1=6
# a,b=0,1
# # print("fibonacci series")
# for i in range(n1):
#     print(a,end="")
#     a,b=b,a+b

# num=7
# count=0
# for i in range(1,num+1):
#     if num%i==0:
#         count+=1
# if count==2:
#     print(i)
# else:
#     print('no')
        
# num=157
# s1=len(str(num))
# total=sum(int(digit)**s1 for digit in str(num))
# if total==num:
#     print('arm')
# else:
#     print('no')

# s1='madam'
# rev=''
# for ch in s1:
#     rev=ch+rev
# if s1==rev:
#     print('palindrome')
# else:
#     print('no')

# s1='sairabanu'
# vowel='aeiou'
# vowels_count=0
# consonants_count=0
# for ch in s1:
#     if ch in vowel:
#         vowels_count+=1
#     else:
#         consonants_count+=1
# print(vowels_count,consonants_count)

# def num(a=5,b=6):
#    print(a+b)
# num(4,5)


# for i in range(1,500):
#   power=len(str(i))
#   total=sum(int(digit)**power for digit in str(i))
#   if total==i:
#       print(i)    

# a,b=5,6
# temp=b
# b=a
# a=temp
# a,b=b,a
# print(a,b)

# s1='SAIRAbanu'
# upper_count=0
# for ch in s1:
#     if ch.islower():
#         upper_count+=1
# print(upper_count)


