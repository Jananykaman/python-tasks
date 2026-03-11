"""
#return function
def square(x):
    return x*x
a=square(5)
print(a)

#lambda function
add=(lambda a,b:a+b)
print(add(5,5))
"""
"""
#map,filter,sorted,reduce
#map
a=[1,2,3,4,5]
res=list(map(lambda x:x*2,a))
print(res)

a=[1,2,3,4,5,6,7]
r=tuple(filter(lambda x:x%2==0,a))
print(r)
 """
"""
a=['apple','2','3','orange','kiwi']
j=sorted(a,key=lambda x:len(x))
print(j)

add=lambda x,y:x+y
print(add('apple','orange'))
print(add(5,7))
print(add('1','apple'))
 """

"""
#multiple datatype
a=[10,"apple", 5.5,"kiwi",1,7,98]
print(sorted(a,key=lambda x:(str(type(x)),x)))

#dictinory based sorting
data={"john":85,"emi":92,"sam":78}
print(sorted(data))
print(sorted(data.items(),key=lambda x:x[1]))
"""

"""
a=[8,9,1,2,10]
res=list(filter(lambda x:x>0,a))
print(max(res))

a=[35,11,8,14,3,9,7,28,9]
res=list(filter(lambda x:x%7==0,a))
print(res)

a=[8,9,1,2,10]
maximum=max(map(lambda x:x,a))
print(maximum)

a=[8,9,1,2,10]
res=list(map(lambda x:max(a),a))
print(res)
"""
