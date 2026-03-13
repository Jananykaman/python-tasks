"""
class student:
    def __init__(self):
        print("Welcome to the student class")
s=student()
"""

"""
#without constructor
class students:
    def demo(self,name,age):
        self.name=name
        self.age=age
s1=students()
s1.demo("Mario",23)
print(s1.name)
print(s1.age)


#parametrized constructor
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
S=Student("Muruga",21)
print(s.name)
print(S.age)
"""
#single inheritance
class parent:
    def demo(self,name,age):
        self.name=name
        self.age=age
class child(parent):
    def demo1(self,salary):
        self.salary=salary
c=child()
c.demo("Mario",23)
c.demo1("25000")
print(c.name)
print(c.age)
print(c.salary)

#multiple
class parent:
    def demo1(self,a,b):
        self.a=a
        self.b=b
class child1(parent):
    def add(self,a,b,c):
        self.c=c
class child2(parent):
    def sub(self,a,b,d):
        self.d=d
c1=child1()
c1.demo1(10,8)
print(c1.a)
print(c1.b)
c1.add(10,8,18)
print(c1.c)
c2=child2()
c2.sub(10,8,2)
print(c2.d)

class parent:
    def demo1(self,a,b):
        self.a=a
        self.b=b
class child1(parent):
    def add(self,a,b,c):
        self.c=c
class child2(child1):
    def sub(self,a,b,d):
        self.d=d
C1=child1()
c1.demo1(10,8)
print(c1.a)
print(c1.b)
c1.add(10,8,18)
print(c1.c)
c2=child2()
c2.sub(10,8,2)
print(c2.d)


















