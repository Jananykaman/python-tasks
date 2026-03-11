"""
#while
fact=1
i=1
n=int(input("Enter n value:"))
while i<=n:
    fact*=i
    i=i+1
print(fact)
"""

"""
#reverse
i=10
while i>0:
    print(i)
    i=i-1
"""

"""
#count the digit
a=int(input("Enter a number:"))
count=0
rem=0
while a>0:
    b=a%10
    rem=rem*10+b
    a=a//10
    count+=1
print(count)
"""

"""
#sum of natural num
i=0
sum=0
n=int(input("Enter a number:"))
while i<=n:
    sum+=i
    i=i+1
print(sum)
"""

"""
a=int(input("Enter a number:"))
rem=0
while a>0:
    b=a%10
    rem=rem*10+b
    a=a//10
else:
    if rem==a:
        print("palindrome")
    else:
        print("not palindrome")
"""

"""
#prime number upto 50
for num in range(1, 51):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
"""

"""
#print 1 to 50 odd number
n=int(input("Enter a number:"))
i=1
while i<=n-1:
    i=i+1
    if i%2==0:
        continue
    print(i)
"""

"""
#skip vowels in string
vowels=['a','e','i','o','u']
string=str(input("Enter a string:"))
i=0
while i<len(string):
    if string[i].lower() in vowels:
        i = i + 1
        continue
    print(string[i],end='')
    i=i+1
"""

"""
#skip neg value in list
a=[10,-5,20,-3,30,-90]
i=0
print("positive value")
while i<len(a):
    if a[i]<0:
        i=i+1
        continue
    print(a[i])
    i=i+1
"""

"""
#print numbers divisible by 5
n=int(input("Enter a number:"))
i=0
while i<n+1:
    i=i+1
    if i%5!=0:
        continue
    print(i)
"""

"""
#stop when user enter 0
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    print("You entered:", num)
print("Loop stopped!")
"""

"""
#stop when the number is 90
a=[10,20,30,40,90,80,70]
i=0
while i<len(a):
    if a[i]==90:
        break
    print(a[i])
    i=i+1
while num <= 50:
"""

"""
#prime number using break
num = 2
    i = 2
    while i < num:
        if num % i == 0:
            break
        i += 1
    if i == num:
        print(num)
    num += 1
"""
