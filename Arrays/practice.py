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





































