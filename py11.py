#02.03.26
#part 1
#pos 0r neg
"""
num = int(input("Enter a number: "))
if num>0:
    print("positive number")
else:
    print("negative number")
"""
"""
#even or odd
a=int(input("Enter a number: "))
if a%2==0:
    print("even number")
else:
    print("odd number")
"""
"""
#largest of two numbers
a=int(input("Enter a value: "))
b=int(input("Enter b value: "))
if a>b:
    print("a is greater than b")
else:
    print("b is greater than a")
"""
"""
#largest of three numbers
a=int(input("Enter a value: "))
b=int(input("Enter b value: "))
c=int(input("Enter c value: "))
if a>b and a>c:
    print("a is greater")
elif b>c:
    print("b is greater")
else:
    print("c is greater")
"""
"""
#div by 5 and 11
i=int(input("Enter a number: "))
if i%5==0 and i%11==0:
    print("The number is divisible by 5 and 11")
else:
    print("The number is not divisible by 5 and 11")
"""
"""
#leap year
a=int(input("Enter a number: "))
if (a%2==0 and a%100!=0) or a%100==0:
    print("leap year")
else:
    print("Not a leap year")
"""
"""
#vowel or consonant
a=str(input("Enter a number: "))
b="AEIOUaeiou"
if a in b:
    print("ch is vowel")
else:
    print("ch is consonant")
"""
"""
#div by 3 and 7
a=int(input("Enter a number: "))
if a%3==0 and a%7==0:
    print("The number is divisible by 3 and 7")
else:
    print("The number is not divisible by 3 and 7")
"""
"""
#Three digit number
a=int(input("Enter a number: "))
x=int(input("Enter a number: "))
if x>=100 and x<=999:
    print("x is three digit number")
else:
    print("x is not three digit number")
"""
"""
#no greater than 100
z=int(input("Enter a number: "))
if z>100:
    print(z,"is greater than 100")
else:
    print(z,"is less than 100")
"""
#prime or not
num = int(input("Enter a number: "))
count = 0
for i in range(1, num + 1):
    if num % i == 0:
        count += 1
if count == 2:
    print("Prime number")
else:
    print("Not a prime number")

#palindrome
num = int(input("Enter a number: "))
temp = num
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
if temp == rev:
    print("Palindrome number")
else:
    print("Not a palindrome")

#Armstrong number
num = int(input("Enter a number: "))
temp = num
sum = 0
while num > 0:
    digit = num % 10
    sum = sum + digit**3
    num = num // 10
if temp == sum:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

#second largest
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if (a > b and a < c) or (a > c and a < b):
    print("Second largest:", a)
elif (b > a and b < c) or (b > c and b < a):
    print("Second largest:", b)
else:
    print("Second largest:", c)

#perfect number or not
num = int(input("Enter a number: "))
sum = 0
for i in range(1, num):
    if num % i == 0:
        sum += i
if sum == num:
    print("Perfect number")
else:
    print("Not a perfect number")

#character is digit or number
ch = input("Enter a character: ")

if ch.isalpha():
    print("Alphabet")
elif ch.isdigit():
    print("Digit")
else:
    print("Special Character")

#div by 3 and 5
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5")
else:
    print("Not divisible by both")

#vowel or not
text = input("Enter a string: ")
if text[0].lower() in "aeiou":
    print("Starts with vowel")
else:
    print("Does not start with vowel")

#find grade using ladder
marks = int(input("Enter marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
elif marks >= 35:
    print("Grade D")
else:
    print("Fail")

#num between 50 to 100
num = int(input("Enter a number: "))
if num >= 50 and num <= 100:
    print("Number is between 50 and 100")
else:
    print("Number is not between 50 and 100")





























































