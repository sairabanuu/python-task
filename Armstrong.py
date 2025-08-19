num=int(input("enter a no:"))
power=len(str(num))
total=sum(int(digit)**power for digit in str(num))
if total==num:
    print("Armstrong number")
else:
    print("not arnstrong number")
    
    #--------------or--------------
    
def is_armstrong(num):
    power=len(str(num))
    total=sum(int(digit)**power for digit in str(num))
    return total==num
print(is_armstrong(153))
print(is_armstrong(123)) 