"""
#tuple functions
a=(1,2,3,4,1,2)
print(a)
b=list(a)
print(b)
print(a.count(1))
print(a.index(2))
print(b.count(2))
print(a.remove(1))
print(a)
"""

"""
#string functions
a="janany"
print(a)
print(a.upper())
print(a.lower())
print(a.count("j"))
print(a.index("j"))
print(a.capitalize())
print(a.title())
print(a.strip())
print(len(a))
print(a.find("j"))
print(a.split())
print(a.replace("y","i"))
"""
"""
words = ["Hello", "Python", "World"]
result = " ".join(words)
print(result)
"""

"""
#set
a={1,3,2,4,7,5}
b={8,9}
print(a)
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(len(a))
print(a.discard(2))
print(a)
print(sum(a))
"""

"""
x={"name":"janany","age": 22,"city":"madurai"}
print(x["name"])
print(x["age"])
print(x)
print(x.items())
print(x.keys())
print(x.values())
print(x.popitem())
print(x)
print(x.pop("name"))
y=x.copy()
print(y)
"""

"""
#operators
#arithmetic operator
a=int(input("Enter a number:"))
b=int(input("Enter b number:"))
print("sum =",a+b)
print("product =",a*b)
print("difference=",a-b)
print("division =",a/b)
print("modulo =",a%b)
print("exponent =",a**b)
print("floor =",a//b)
"""

"""
#Assignment operator
a=int(input("Enter a number:"))
b=int(input("Enter b number:"))
a+=b
print(a)
a-=b
print(a)
a*=b
print(a)
a=b
a/=b
print(a)
"""

"""
#comparision operator
a=int(input("Enter a number:"))
b=int(input("Enter b number:"))
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
"""

"""
#logical operator
a=int(input("Enter a number:"))
b=int(input("Enter b number:"))
print(a and b)
print(a or b)
print(not a)
"""

"""
#bitwise operator
a=int(input("Enter a number:"))
b=int(input("Enter b number:"))
print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(~b)
print(a<<1)
print(a>>5)
print(b>>1)
print(b<<1)
"""

"""
#divisibility of number 5 and 7
count1=0
count2=0
for i in range(5,100):
    if i%5==0:
        count1+=1
    if i%7==0:
        count2+=1
print("count1=",count1)
print("count2=",count2)
"""

"""
#odd or even
a=int(input("Enter a number:"))
if(a%2==0):
    print("The number is divisible by even number")
else:
    print("The number is divisible by odd number")
"""

"""
#positive or negative
a=int(input("Enter a number:"))
if(a>0):
  print("The number is positive")
else:
 print("The number is negative")
"""

"""
print(True+True)
print(False+False)
print(True*False)
print(False*False)
"""
