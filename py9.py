"""
#task
import math
print(int(math.sqrt(25)))

from math import sqrt
print(int(sqrt(25)))

import math as m
print(int(m.sqrt(25)))

import math as m
print(int(m.factorial(5)))
print(int(m.pow(2,3)))

import math
print(dir(math))

import math
help(math.sqrt)
help(math.pow(2,3))

#TASK
#frequency count
#method 1
import math
a=[2,4,6,2,8,9,4,1]
b={}
for i in a:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
print(b)

#method 2
from collections import Counter
a=[2,4,6,2,8,9,4,1]
b=Counter(a)
print(b)

#duplicate value
def duplicate():
    a=[1,2,3,4,6,5,6,8,3,2]
    b=[]
    for i in a:
        if i not in b:
            b.append(i)
    print(b)
duplicate()

#palindrome
def palindrome():
    a=str(input("Enter a string:"))
    rev=""
    for i in a:
        rev=i+rev
    print(rev)
    if a==rev:
        print("is palindrome")
    else:
        print("is not palindrome")
palindrome()

#list filtering
def filtering():
    a=[1,2,3,4,5,6,7,8,9]
    b=list(filter(lambda x:x%2==0,a))
    print(b)
    c=list(filter(lambda x:x%2!=0,a))
    print(c)
filtering()

#prime
def prime(a,b):
    for num in range(a, b+1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                print(num)
prime(1, 100)

#second_largest
def second_largest():
    a = [23,45,67,13,47,99,100]
    a.sort()
    print("Second_largest number is:", a[-2])
second_largest()

#greater than 10
a=[5,1,7,18,3,20]
r=list(filter(lambda x:x>10,a))
print(r)
"""

#armstrong number
def armstrong(num):
    power = len(str(num))
    total = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        total += digit ** power
        temp //= 10
    if total == num:
        return "Armstrong Number"
    else:
        return "Not Armstrong"
print(armstrong(153))


