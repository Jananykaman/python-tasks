"""
#control flow statements
# Program to analyze numbers from 1 to 10
print("Starting Program...\n")
for i in range(1, 11):  # for loop
    # break statement
    if i == 9:
        print("Stopping loop at 9")
        break
    # continue statement
    if i == 5:
        print("Skipping number 5")
        continue
    # if-elif-else
    if i % 2 == 0:
        print(i, "is Even")
    elif i % 3 == 0:
        print(i, "is Divisible by 3")
    else:
        print(i, "is Odd")
# while loop
print("\nNow using while loop")
count = 1
while count <= 3:
    # nested if
    if count > 0:
        if count == 2:
            pass  # pass statement (does nothing)
        print("Count:", count)
    count += 1
print("\nProgram Ended")
"""

"""
#Decision making statement
# if-else statement
a=int(input("Enter a number:"))
if(a%2==0):
    print("The number is divisible by even number")
else:
    print("The number is divisible by odd number")
"""

"""
x=int(input("Enter x number:"))
if x%5==0 and x%7==0:
    print("It is divisible by a and b")
else:
    print("It is not divisible by a and b")
"""

"""
password="janany"
a=str(input("Enter a string:"))
if a==password:
    print("The password is correct")
else:
    print("The password is incorrect")
"""

"""
a=int(input("Enter a speed:"))
if a<80:
    print("The speed is safe")
elif a>90:
    print("The speed is not safe")
else:
    print("The speed is safe")
"""

"""
a=str(input("Enter a password:"))
b=len(a)
if b>8:
    print("The password is valid")
else:
    print("The password is invalid")
"""

"""
a=int(input("Enter a number:"))
if a>1000:
    print("Discount")
else:
    print("No Discount")
"""

"""
salary=int(input("Enter a number:"))
if salary>50000:
    print("bonus provided")
else:
    print("No bonus provided")
"""

"""
#elif statement
day=int(input("Enter a day:"))
if day==1:
    print("The day is sunday")
elif day==2:
    print("The day is monday")
elif day==3:
    print("The day is tuesday")
elif day==4:
    print("The day is wednesday")
elif day==5:
    print("The day is thursday"):
elif day==6:
    print("The day is friday"):
elif day==7:
    print("The day is saturday"):
else:
    print("The day is not valid data")
"""

"""
j=int(input("Enter a value:"))
k=int(input("Enter a value:"))
n=str(input("Enter a value:"))
if n=='add':
    print(j+k)
elif n=='subtract':
    print(j-k)
elif n=='multiply':
    print(j*k)
elif n=='divide':
    print(j/k)
elif n=='power':
    print(j**k)
elif n=='mod':
    print(j%k)
elif n=='floor':
    print(j//k)
else:
    print("Calculations can't be performed")
"""

"""
light=str(input("Enter a lightness:"))
if light=='red':
    print("stop")
elif light=='green':
    print("go")
elif light=='yellow':
    print("wait")
"""

"""
season=str(input("Enter a season:"))
if season=='summer':
    print("The season is more hot")
elif season=='autumn':
    print("The season is autumn")
elif season=='winter':
    print("The season is winter")
else:
    print("The season is spring")
"""

"""
#Nested if
cost=100
c=int(input("Enter a cost:"))
if c>=cost:
    d = str(input("Enter a operation:"))
    if d=='withdraw':
        print("The cost is withdraw")
    else:
        print("The cost is not withdraw")
else:
    print("you cannot withdraw")
"""

"""
age=int(input("Enter a age:"))
if age>=21:
    degree=str(input("Enter a degree:"))
    if degree=='BE':
        print("valid degree is BE")
    else:
        print("invalid degree ")
else:
    print("invalid age")
"""

"""
username=str(input("Enter a username:"))
if username=="Janany":
    password=str(input("Enter a password:"))
    if password=="janany123":
        print("The password is valid")
    else:
        print("The password is not valid")
else:
   print("The username is not valid")
"""


"""
a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
c=int(input("Enter c value:"))
if a > b:
    if a > c:
        print("Largest number is:", a)
    else:
        print("Largest number is:", c)
else:
    if b > c:
        print("Largest number is:", b)
    else:
        print("Largest number is:", c)
"""
"""
num=int(input("Enter a number:"))
if num>0:
    print("number is positive")
    if num%2==0:
        print("even")
    else:
        if num%3==0:
            print("The number is divided by 3")
        else:
            print("not divisible by 3")
else:
    print("Number is negative number")
"""

"""
mark=int(input("Enter a mark:"))
if mark>=50:
    if mark>=90:
        print("grade A")
    else:
        if mark>=75:
            print("grade B")
        else:
            print("grade C")
else:
    print("fail")
"""

"""
year=int(input("Enter a year:"))
if year%4==0:
    if year%100!=0 or year%400==0:
        print("The year is leap year")
    else:
        print("The year is not leap year")
else:
    print("The year is not leap year")
"""
