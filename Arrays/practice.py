x=10
y=x
x=20
y=x
print(y)

# ✅ Valid variable names
name="raj"
print(name)
age_1=25
print(age_1)
_private=True
print(_private)
myName="hello"
MY_CONSTANT=200
print(MY_CONSTANT)

#invalid varname
# 1name="sachin"
# my-name="sachin"
# class="python"
# my name = "Raj"

# Python has the following **built-in data types:**
Numbers=int,float,complex
Text=str
Boolean=bool
Sequence=list,tuple,range
Mapping=dict
Set=set,frozenset
NoneType=None

# print(type(Numbers))
print(Numbers)
print(Text)
print(bool)
print(Sequence)

x=10
y=-5
z=10_00_000 #__ for readability (python 3.6+)
print(z)
print(type(x))

# Python handles arbitrarily large integers
big_number=99999999999999999999999999999999999999
print(big_number+1)

binary=0b101010
print(binary)

#different number bases
binary=0b1010
print(binary)
octal=0o12
print(octal)

print(5,"5")
x=10
print(x)

# Q1: What is the difference between is and ==?
a=[1,2,3]
b=[1,2,3]
print(a == b)
print(a is b)

#immutable
str_value="hello"

list_value=list(str_value)
list_value[0]='J'
print("".join(list_value))



#mutable
list_value=[1,3,4,5]
list_value[0]=11
print(list_value)

set_value={1,3,4,5}

#set is a distinct collection of unordered element
A={1,2,3,4,5}
B={4,5,6}
print(A | B)

#intersection common element
A={1,2,3,4,5}
B={3,4,5,6}
print(A & B)

# and is the & is intersection operator in python

print(A-B) #difference element in a not in b

#complement element not in A from the universal element 
A={1,2,3,4,5,6,7,8}
U = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}  
print(U-A)

#subset
A={1,2,8,4,5,6}
c={1,2,3}
print(c.issubset(A))

empty=set()
print(empty)
print(type(empty))
print(len(empty))
empty.add(10)
empty.add(10)
print(len(empty))


#octal 
octal_con=0o12
print(octal_con)
hex_dec=0x12
print(hex_dec)

#float
x=3.14
y=-2.5
z=1.0
scientific_not=1.5e3
print(type(x))
print(type(scientific_not))

print(0.1+0.2) #float are stored in binary it create the precision issues
print(0.1+0.2==0.30000000000000004)

#correct way to compare float
import math
print(math.isclose(0.1+0.2,0.3))

print(math.isclose(0.1+0.2,0.3))

print(round(0.2+0.1,1)==0.3)

# use decimal for precision
from decimal import Decimal
print(Decimal('0.1')+Decimal('0.2'))

#complex
c=3+4j
print(c.real)
print(c.imag)
print(type(c))

print(isinstance(True,int))
print(True==1)
print(True==0)
print(False==0)
print(True+True)
print(True*5)
print(False+1+1)

#this mean
print(True>False)
print(sorted([False,True,False,True,False,True]))

val=0j
print(type(val))

print(bool(1))
print(bool(0))
print(bool(""))
print(bool([]))
print(bool({}))
print(bool(None))

print(bool("hi"))
print(bool([0]))
print(bool(" "))

#string are immutable
name="Python"
print(type(name))
print(name[0])
print(name[-1])
print(name[0:3])
print(name[-1])
print(name[::-1])

#list
fruits=["apple","banana","cherry"]
print(type(fruits))
mixed  = [1, "hello", 3.14, True, None]
print(mixed[0])
print(mixed[2])
mixed[0]=12
print(mixed)

nested=[[1,2],[3,4]]
print(nested[0])
print(nested[1])


#tuple 
tuple_value=(1,2,3)
print(type(tuple_value))
single=(42,)
print(type(single))
empty=()
print(type(empty))

name={
    "name":"Raj",
    "city":"Beng",
    "age":25
}
name["name"]="sham"
print(name["name"])
print(type(name))

#NoneType datatype
x=None
print(type(x))
print(x is None)

#type conversion (casting)
x=1
y=5.0
print()
print(type(x+y))


# Explicit Conversion (you do it manually)
print(type(int("42")))
print(type("42"))
print(int(3.9))
print(3.9)
# print(int("3.9")) #floating point string will not give the conversion

print(type(int(float("3.4"))))

#input/output

print("hello")
print("a","b","c",sep="-")
print("hello",end=" ")
print("world",end=" ")
print("Hey")

# value=input("Enter the input")
# print(type(value))

# value=input("enter age")
# v1=int(value)
# print(type(v1))

# v1=input("Enter the age")
# v2=input("Enter the age2")
# print(type(int(v1)+int(v2)))

a=b=c=0
print(a,b,c)

#tuple unpacking
a,b,c=11,22,33
print(a)
print(b)
print(c)

# Swap without temp variable
a=10
b=20
b,a=a,b
print(a,b)

# Extended unpacking
first,*last=[1,2,3,4,5]
print(first)
print(last)

*beginning,last=[1,2,3,4,5]
print(beginning)
print(last)

first,*middle,last=[1,2,3,4,5]
print(first)
print(middle)
print(last)

x=256
y=256
print(x is y)

x=1000
y=1000
print(x is y)



x=257
y=257
print(x is y)
print(x == y)

a=100000
b=100000
print(a == b)
print(a is b)

# Created dynamically at runtime
x=int("10000000")
y=int("10000000")
print(x is y)
print(x == y)


x=int("10000000000000000000000")
y=int("10000000000000000000000")
print(x is y)

import dis
def test():
    a=10000
    b=10000
    print(a is b)
dis.dis(test)

x=257
y=257
print(x is y)

x=int("257")
y=int("257")
print(x is y)


x=int("123")
y=int("123")
print(x is y)

print(True+True+False)
print()

def process(value=[]):
    value.append(1)
    return value
print(process())
print(process())


def process(value=None):
    if value is None:
        value=[]
    value.append(1)
    return value
print(process())
print(process())
print(process())


a=b=[]
a.append(1000)
print(b)

print(isinstance(True,int)) #True

x=None
print(type(x))
print(x==None)
print(x is None)

#string
name="python"
name='python'
name10="""triple double"""
print(name10)

n=42
print(type(str(n)))

name=str()
print(len(name))

s6=str()
print(type(s6))

# String concatenation in a loop is SLOW
# res=""
# for i in range(100000):
#     res+=str(i)

res="".join(str(i) for i in range(10000))


words=["Hello","My","name","is","python"]
result="".join(words)
print(result)

sen="Hello","world"
res="".join(sen)
print(res)

sen="Hello world"
print(" ".join(sen))

words=["Hello","My","name","is","python"]
print(", ".join(words))

# 2. Join with hyphen
words=["Hello","My","name","is","python"]
res="-".join(words)
print(res)

#join with no sep
words=["Hello","My","name","is","python"]
print("".join(words))

words="Hello","My","name","is","python"
print("".join(words))

numbers=[1,2,3,4,5]
res="".join([str(n) for n in numbers])
print(res)

text="Hello world"
#split into the list
words=text.split()
print("".join(words).upper())

text="Hello world"
print("-".join(text))

text="Hello world"
word=text.split()
print("_".join(word))

s1="Hello"
print(s1*3)

#membership
s1="hello"
print("ell" in s1)
print("xyz" not in s1)

# newline
# print("Hello\nworld")
print("hello\tworld")

# quotes inside string
print("Hello\"Hi\"")

# backslash
print("C:\\Users\\name")

print("c:\\username\\name")
print("c:\\username\\user")

# carriage return
print("Hello\rworldssss")

#unicode
print("\u0041")
print("\u0099")
print("\u0087")
print("\u0032")


#string formatting %s -> string, %f-> float, %d->int, %.2f->float with 2decimal value

name="Raj"
age=25
print("my name is %s and %d years old" %(name,age))

name="Dhanu"
age=34
city="mumbai"
print("my name is %s and i am %d age old and from %s" %(name,age,city))

name="Raj"
age=25
print("my name is {} and i am {} old".format(name,age))
print("my name is {0} and i am {1} old".format(name,age))
print("my name is {name} and i am {age} old".format(name=name,age=age))

# Formatting numbers
print("{:.2f}".format(300000.1444444))
print("{:10}".format("hello")) #width 10
print("{:>10}".format("hello")) #right align
print("{:<10}".format("Hello")) #left align
print("{:^100}".format("helloworld"))    # (center align)


#  f-strings 
name="Raj"
age=27
city="navi mumbai"
print(f"my name is {name} and age is {age} and belongs to the {city}")
print(f"my name is sachin{name} and age is {age+2}")

# Formatting numbers 3.14
pi=3.1434
print(f"PI={pi:.2f}")
print(f"PI={pi:10.2f}")
print(f"{10000000:,}")

print(f"{0.25:.0%}")

s="hello sachin"
print(s.upper())
print(s.lower())

# ← capitalizes first letter of each word
print(s.title())

#only first letter of the string used capitalized
print(s.capitalize())


s="Hey this is sachin"
print(s.swapcase())

s="Hey this is sachin"
print(s.title())

s="Hey's this is see"
print(s.title())

#multiline f-string
msg={
    f"name:{name}\n"
    f"age:{age}\n"
    
}
print(msg)

from string import Template
t=Template("Hello $name and $age")
print(t.substitute(name="Raj",age=25))

#search and check method
s="Hello world HEllo"
#  ← index of FIRST occurrence, -1 if not found
print(s.find("Hello"))
print(s.find("hello"))
print(s.find("world"))

print(s.rfind("World"))
print(s.rfind("HEllo")) #index of the last occurrence

print(s.index("HEllo")) #index of the like fund() but raise the value error if not found
# print(s.index("HEllo")) #raise value error if not found

s="Hello Hey Hello sachin"
print(s.count("Hello"))

s="Hello"
print(s.count('l'))

s="Hello Hey this is sachin"
print(s.startswith("Hey"))
print(s.startswith("Hello"))
print(s.endswith("sachin"))

print(s.startswith(("Hi","Hello"))) #tuple of prefix



#check type method (return True/False)
print("123".isdecimal())
print("123".isdigit())
print("\u00B2".isdigit())
print("\u00B2".isdecimal())
print("123abc".isalnum())
print("123222".isdecimal()) #is decimal only return true when it should contains all the digits not . 
print("1234.90".isdigit())
print("1234".isalpha())
print("H12344".istitle())



# Strip Methods

s="    Hello    "
print(s.strip())
print(s.rstrip())
print(s.lstrip())

s="Hello world"
print(s.strip())

words=s.split()
print("".join(words))

s="#######Hello world#####"
print(s.strip("#"))
print(s.strip("#H"))
print(s.strip("#d"))

#replace method
s="Hello world Hello"
print(s.replace("Hello","Hi"))
print(s.replace("Hello","Hi",1))

#split method
s="Hello, world, Hey"
print(s.split(","))
print("a,b,c".split(","))
print("a,,b,,c".split(","))
print("a b c".split())
print("a b c".split(" ",1)) #split only one space

# rsplit (split from right)
print("a b c".rsplit(" ",1))

world="Hello world" #join only work with string 
w=world.split()
print("".join(w))

s=['a','b','c']
print("".join(s))

n=[1,2,3,4,5]
print("".join(str(num) for num in n))

# Alignment & Padding Methods
s="hello"
print(s.center(11))
print(s.center(15,"-"))
print(s.ljust(10))
print(s.rjust(10))
print(s.zfill(11))

#partition
s="HEllo world"
print(s.partition(" "))

print(s.partition("x"))


#string interned

a="hello"
b="hello"
print(a==b)
print(a is b)

a="helloooooooooooooooooooooooooooooooo"
b="helloooooooooooooooooooooooooooooooo"
print(a is b)

a=256
b=256
print(a is b)
print(a==b)

a=257
b=257
print(a is b)

a=1000
b=1000
print(a is b)

#has space - not interned
a="hello world"
b="hello world"
print(a is b)

#has special char not interned
a="hello@123"
b="hello@123"
print(a is b)

import sys
a=sys.intern("hello world")
b=sys.intern("hello world")
print(a is b)

a="Hey this is"
b="Hey this is"
print(a is b)


# String as Sequence
s="Python"
print(len(s))

#Iteration
for ch in s:
    print(ch,end=" ")
print()
#enumerate the value
st_value="Python"
for i,ch in enumerate(st_value):
    print(i,ch)
    
#basic for loop

for i in range(5):
    print(i)
    
#list of value
list_value=["apple","banana","orange"]
for fruit in list_value:
    print(fruit)

for i in range(len(list_value)):
    print(list_value[i],end=" ")
print()  
# 3. For Loop with String
s="Hey"
for ch in s:
    print(ch,end=" ")
print()
fruits=["apple","banana","mango"]
for i,fruit in enumerate(fruits):
    print(i,fruit)

#for loop with range
for i in range(0,10,2):
    print(i,end=" ")
print()
for i in range(10,0,-1):
    print(i,end=" ")

print()
# For Loop with Dictionary
person={"name":"sachin","age":25}
for key in person:
    print(key,end=" ")
# for k,v in person.items():
#     print(k,v,end=" ")

print()
for key in person:
    print(key,end=" ")
print()
for key,value in person.items():
    print(key,value,end=" ")
print()    
for value in person.items():
    print(value,end=" ")

print()
for key in person.keys():
    print(key,end=" ")
print()
for values in person.values():
    print(values,end=" ")
print()
for key,values in person.items():
    print(key,values,end=" ")
print()    
    
#nested for loop
for i in range(3):
    for j in range(3):
        print(i,j)

#for loop with zip() -2 list write together
names=["alen","bob","kummu"]
ages=[12,22,22]
for name,age in zip(names,ages):
    print(name,age,end=" ")

#list comprehension one line for loop

square=[]
for i in range(5):
    square.append(i**2)
print(square)

square=[i**2 for i in range(5)]
print(square)


#for loop with break and continue
for i in range(5):
    if i==5:
        break
    print(i)
print()
# continue — skip current iteration
for i in range(5):
    if i==3:
        continue
    print(i)

def add(a,b):
    return a+b
print(add(10,20))

add=lambda a,b: a+b
print(add(2,3))

#lambda with map() map with each element
number=[1,2,3,4,5]
res=list(map(lambda x:x**2,number))
print(res)

#lambda with reduce() accumulate 1 2 3 4 5 = 15
from functools import reduce
num=[1,2,3,4,5]
res=reduce(lambda x,y: x+y,num)
print(res)

#lambda with condition if/else 
check=lambda x: "even" if x%2==0 else "odd"
print(check(2))

s="Python"
print("Pyth" in s)

print(min('Hello')) #lowest unicode value
print(max('Hello'))

print(sorted('hello'))
num=[1,2,3,5,4,7,6]
num.sort()
print(num)
print(sorted(num))

for c1,c2 in zip("abc","ABC"):
    print(c1,c2)

# Reverse a string
s="paper"
print(s[::-1])

s="hello world"
print(s.split())
print(s.split("o"))
print(len(s.split()))

def is_palindrome(s):
    s=s.lower().replace(" ","")
    return s==s[::-1]
s="madam"
print(is_palindrome(s))

s="hello world python"
print(s.split(" ",1)) #it will split at the first space and return the list

print(s.partition(" ")) #return the tuple and always 3 parts

print(bool(" "))
print(bool("")) 

print(0.1+0.2,0.3)
print(0.1+0.2==0.3)

from decimal import Decimal
print(Decimal(.01)+Decimal(0.2)==0.3)

import math
print(math.isclose(0.1+0.2,0.3))
print(round(0.1+0.2,1)==0.3)

import copy
original=[1,2,3,4]
shallow=copy.copy(original)
print(original == shallow)
print(original is shallow)

orig=[1,2,3,4]
shall=copy.copy(orig)
# print(orig == shall)
shall.append(5)
print(orig)
print(shall)
print(orig==shall)
print(orig is shall)  #in shallow it normal does not change the list of original and if it nested it will change


# orig=[1,2,3,4,[5,6]]
# shall=copy.copy(orig)
# shall[0]=99
# shall[4].append(9)
# print(orig)


# #deep copy
# import copy
# orig=[1,2,3,4,5]
# deep=copy.deepcopy(orig)
# print(orig == deep)
# print(orig is deep)

orig=[1,2,3,4,5]
deep=copy.deepcopy(orig)
deep.append(9)
print(orig == deep)

orig=[1,2,3,4,5,[8,9]]
shall=copy.copy(orig)
shall[5].append(10)
print(orig)
print(shall)

orig=[1,2,3,4,5,[8,9]]
deep=copy.deepcopy(orig)
deep[5].append(10)
print(orig)
print(deep)

# Remove duplicates keeping order
lst = [1, 2, 2, 3, 1, 4, 3, 5]
lst.sort()
unique=[]
for i in range(len(lst)):
    if lst[i]!=lst[i-1]:
        unique.append(lst[i])
print(unique)

lst = [1, 2, 2, 3, 1, 4, 3, 5]
unique=[]
for num in lst:
    if num not in unique:
        unique.append(num)
print(unique)

# Remove duplicates keeping order use the form.dict to preserve the order
lst = [1, 2, 2, 3, 1, 4, 3, 5]
print(list(dict.fromkeys(lst)))

# Using set (does NOT preserve order)
lst = [1, 2, 2, 3, 1, 4, 3, 5]
print(list(set(lst)))

nested = [[1, 2], [3, 4], [5, 6]]
res=[x for sublist in nested for x in sublist]
print(res)

def flatten(lst):
    res=[]
    for item in lst:
        if isinstance(item,list):
            res.extend(flatten(item))
        else:
            res.append(item)
    return res    

print(flatten([1, [2, [3, [4]], 5]]))

def find_palindrome(lst):
    n=len(lst)
    l=0;r=n-1
    while l<r:
        if lst[l]!=lst[r]:
            return False
        l+=1
        r-=1
    return True       
lst=[1,2,3,2,1]
print(find_palindrome(lst))

#rotate array
def rotate_array(lst,k):
    n=len(lst)
    rotation=k%n
    
    for _ in range(0,rotation):
        e=lst.pop()
        lst.insert(0,e)
    return lst    
lst=([1,2,3,2,1,7,8])
k=2
print(rotate_array(lst,k))

lst = [1, 2, 2, 3, 1, 4]
print(list(dict.fromkeys(lst)))

lst = [0, 1, 2, 3, 4]
print(lst[10:30])
print(lst[3:1])

even=[x for x in range(10) if x%2==0]
print(even)


even=[x if x%2==0 else -x for x in range(10)]
print(even)   

lst = [[0]*3]*3
print(lst)
lst[0][0]=1
print(lst)

lst=[[0]*3]*3
lst=[[0]*3 for _ in range(3)]
lst[0][0]=1
print(lst)


lst = [1, 2, 3, 4, 5]
for i in lst:
    lst.remove(i)
print(lst)

if []:
    print('yes')
if [0]:
    print('yes')

# 5. List unpacking
a,b,c=[1,2,3]
print(a)
print(b)
# a, b = [1, 2, 3]

# 6. Concatenation vs extend
num=[1,2,3,4]
num=num+[5,6]
print(num)

num=[1,2,3,4]
num+=[23]
print(num)

lst = [0, 1, 2, 3, 4]
print(lst[3:1])
print(lst[1:3])
print(lst[:3])
print(lst[1:2])

#second largest
def second_largest(arr):
    max=arr[0]
    sec_max=float('-inf')
    for num in arr:
        if num>max:
            sec_max=max
            max=num
        elif num>sec_max and num!=max:
            max=sec_max
    return sec_max
lst = [0, 1, 2, 3, 4]
print(second_largest(lst))

#second largest
def second_largest(arr):
    unique=list(set(arr))
    unique.sort()
    return unique[-2]    
lst = [0, 1, 2, 3, 4]
print(second_largest(lst))

import sys
lst=[]
print(sys.getsizeof(lst))
lst = [1, 2, 3, 4, 5]
print(sys.getsizeof(lst))

import array
int_array=array.array('i',[1,2,3,4,5,6])
print(int_array)
int_array.append(9)
print(int_array)

# Sort by last character of name
names = ["banana", "apple", "cherry", "kiwi"]
names.sort(key=lambda x:x[-1])
print(names)

# Sort strings case-insensitively
names = ["Banana", "apple", "Cherry"]
names.sort()
names.sort(key=str.lower)
names.sort(key=lambda x: x.lower())
print(names)

data = [(1, 'b'), (2, 'a'), (1, 'a'), (2, 'b')]
data.sort(key=lambda x: x[0])
print(data)

# List as Stack and Queue LIFO 
stack=[]
stack.append("a") #both used O(1)
stack.append("b")
stack.append("c")
print(stack)
stack.pop()
stack.pop()
print(stack)

# from collections import deque
# queue=deque
# queue.append("a")
# queue.append("b")
# queue.popleft()

#FIFO
queue=[]
queue.append("a")
queue.append("b")
queue.pop(0)
print(queue)


a,*_,b=[1,2,3,4,5]
print(a,b)

#unpack in pair
pair=[(1,'a'),(2,'b'),(3,'c')]
for num,ch in pair:
    print(num,ch)
    
#move zeros
def move_zeros(lst):
    non_zeros=[x for x in lst if x!=0]
    zeros=[0]*(len(lst)-len(non_zeros))
    return non_zeros+zeros
    
lst=[1,2,3,4,0,5,0,6]
print(move_zeros(lst))








        
    

























































