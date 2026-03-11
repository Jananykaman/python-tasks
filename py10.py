"""file=open("data.txt","w")
file.write("hello world")
file=open("data.txt","r")
print(file.read())"""

"""
#file handling
file=open("data.txt","a")
file.write("hello world")
file=open("data.txt","r")
print(file.read())
file.close()
"""
"""
file=open("data1.txt","w")
file.write("hello world")
file.close()

file=open("data2.txt","a")
file.write("hello world")
file.close()
"""

with open("data.txt","r+") as file:
    file.write("Hai friends")
    file.seek(0)
    print(file.read())

with open("data3.txt","w+") as file:
    file.write("Hai friends")
    file.seek(0)
    print(file.read())

import getpass
username = input("Enter your username: ")
password = getpass.getpass("Enter your password: ")
found=False
with open("user.txt","r") as file:
    for line in file:
        user,pwd = line.strip().split()
        if username==user and password==pwd:
            found=True
            break
if found:
       print("Login successful")
else:
    print("Login Unsuccessful")



















