"""
#user defined function
#positional args
def student(name,age):
    print(name,age)
student("janany",22)

#keyword args
def student(name,age):
    print(name,age)
student(age=22,name="janany")

#default args
def great(name="janany"):
    print("hello",name)
great("jan")

#variable length args
def demo(* degree):
    print(degree)
demo('BE','BCA','MBA','IT')

#student information
def student(name,age,*marks,**info):
    print(name,age,marks,info)
student("Janany",22,99,98,100,city="madurai",blood_group="0",course="python",DOB="30-09-2004")
"""

"""
#function
def demo():
    x=10
    print(x)
demo()
"""

"""
#odd or even
def odev(a,b):
    if (a%2==0):
        print(a,"is even")
    else:
        print(a,"is odd")
    if(b%2==0):
        print(b,"is even")
    else:
        print(b,"is odd")
odev(2,3)

#arithmetic
def arithmetic(x,y):
    print("operations are:")
    print("add",x+y)
    print("sub",x-y)
    print("mul",x*y)
    print("div",x/y)
    print("floor",x//y)
    print("mod",x%y)
    print("power",x**y)
arithmetic(5,5)

#reverse the string
def reverse():
    print("reverse")
    a=str(input("Enter a string:"))
    print(a[::-1])
reverse()

def reverse1():
    a=str(input("Enter a string:"))
    rev=""
    for i in a:
        rev=rev+i
        a.split()
        print(rev)
reverse1()

def reverse1():
    a=str(input("Enter a string:"))
    rev=""
    for i in a:
        rev=i+rev
    print(rev)
    if a==rev:
        print("is palindrome")
    else:
        print("is not palindrome")
reverse1()
"""