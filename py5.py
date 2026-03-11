"""
a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for i in a:
    if i%2==0:
        print(i,'is even')
    else:
        print(i,'is odd')
"""

"""
num=int(input("Enter a number:"))
fact=1
for i in range(1,num+1):
    fact*=i
print(fact)
"""

"""
n=int(input("Enter a number:"))
print("multiplication table")
for i in range(1,11):
    print(i,'*',n,'=',i*n)
"""

"""
#prime number
n=int(input("Enter a number:"))
if n <= 1:
        print("The number is not a prime number")
elif n == 2:
    print("The number is a prime number")
else:
    for i in range(2, n):
        if n%i==0 :
            print(n,"is not prime")
            break
        else:
            print("is prime")
            break
"""

"""
#Task
#print 00 to 99
for i in range(10):
    for j in range(10):
        print(i,j)
"""

"""
#sum of natural numbers
sum=0
n=int(input("Enter a number:"))
for i in range(1,n+1):
    sum+=i
print(sum)
"""

"""
#count vowels in string
vowels=['a','e','i','o','u']
string=str(input("Enter a string:"))
count=0
for c in string:
    if c in vowels:
        count+=1
print(count)
"""

"""
#pyramid pattern
rows=int(input("Enter a row value:"))
for i in range(1,rows):
    for j in range(1,i+1):
        print(j,end='')
    print()
"""