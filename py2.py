#Data types
range(0,10)
a=list(range(10))
print(a)
b=tuple(range(10))
print(b)
c=set(range(10))
print(c)
"""

"""
#list operation
a=[5,3,7,9,1,2]
print(a)
print("max=",max(a))
print("min=",min(a))
print("sum=",sum(a))
print("popped element=",a.pop())
print("sorted elements =",sorted(a))
print("length of list=",len(a))
print("reversed list=",a.reverse())
print(a)
print("appended element=",a.append(4))
print(a)
print("extended element=",a.extend([0,6]))
print(a)
print("inserted element=",a.insert(0,5))
print(a)
print("counted element=",a.count(5))
print(a)
print("sorted list=",a.sort())
print(a)
print("cleared list=",a.clear())
print(a)
"""

"""
#practise
a=['a','d','b','c']
print(a)
print("rev=",reversed(a))
print("max=",max(a))
print("min=",min(a))
print("count=",len(a) )
print("sorted list=",sorted(a))
print("reversed list=",a.reverse())
print(a)


e=5
f=6
g=complex(e,f)
print(int(g.real),int(g.imag))
"""

"""
#10.02.26 PRACTISE
# Grocery list (item, quantity, price)
grocery = [
    ["Rice", 10, 50],
    ["Sugar", 5, 45],
    ["Oil", 2, 120]
]
print("Original List:")
for item in grocery:
    print(item)
# 1. append() → Add item
grocery.append(["Salt", 3, 20])
print("\nAfter append():")
print(grocery)
# 2. insert() → Insert at specific position
grocery.insert(1, ["Tea", 2, 80])
print("\nAfter insert():")
print(grocery)
# 3. len() → Number of items
print("\nTotal items:", len(grocery))
# 4. index() → Find position of item
print("\nIndex of Oil:", grocery.index(["Oil", 2, 120]))
# 5. remove() → Remove specific item
grocery.remove(["Sugar", 5, 45])
print("\nAfter remove():")
print(grocery)
# 6. pop() → Remove using index
grocery.pop(0)
print("\nAfter pop():")
print(grocery)
# 7. sort() → Sort by quantity (using key)
grocery.sort(key=lambda x: x[1])
print("\nAfter sorting by quantity:")
print(grocery)
# 8. reverse() → Reverse list
grocery.reverse()
print("\nAfter reverse():")
print(grocery)
# 9. copy() → Copy list
new_list = grocery.copy()
print("\nCopied List:")
print(new_list)
# 10. clear() → Remove all items
temp = new_list.copy()
temp.clear()
print("\nAfter clear():", temp)
print(grocery)
"""

#odd or even using list
numbers = [12, 7, 5, 20, 33, 18, 0]
even_count = 0
odd_count = 0
for i in numbers:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even numbers count:", even_count)
print("Odd numbers count:", odd_count)
"""
