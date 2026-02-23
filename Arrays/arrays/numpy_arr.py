from numpy import *
arr = array([1,2,3,4,5])
for x in arr:
    print(x,end=" ")
print('\n') 
val=linspace(10,20,5)
for x in val:
    print(x,end=" ")
print('\n')   
v=arange(10,20,2)
for x in v:
    print(x,end=" ")
print('\n')

value12=zeros(10)
for x in value12:
    print(x,end=" ")
print('\n')    
zero =array(10)
print(zero)

ond=array([10,20,30,40])
print(ond)

twod=array([[1,2,3],[4,5,6]])
print(twod)

threed= array([[[1,2,3,4],[5,6,7,8]],[[3,4,5,6],[3,4,5,6]]])
print(threed)
print()

#print even number array
# n=int(input().strip())
# arr=list(map(int,input().split()))[:n]
# for i in range(len(arr)):
#     if arr[i]%2==0:
#         print(arr[i],end=" ")
# print()
# for num in arr:
#     if num%2==0:
#         print(num,end=" ")
#avg of array
# n=int(input().strip())
# arr=list(map(int,input().split()))[:n]
# sum=0
# avg=0
# for i in range(len(arr)):
#     sum+=arr[i]
#     avg=sum/len(arr)
# print(avg) 


import numpy as np
a1=np.array([1,2,3])
a2=np.array([[1,2],[5,6]])
a3=np.array([2,3,5])
print(a1.__sizeof__())
print(a1+2)
print(a1)
print(a1+a3)

#broadcast the value
arr1=np.array([1,2,3])
arr2=np.array([[4],[5],[6]])
print(arr1+arr2)

arr10=np.array([[1,2,3],[4,5,6],[1,2,3],[5,6,7]])
# print(arr10.ndim)
# print(arr10)
arr11=np.array([2,3,4])
print(arr10+arr11)

old=['a','b','c','b','d','e']
# rem_dup=list(set(old))
val=[]
for item in old:
    if item not in val:
        val.append(item)        
print(val)

import numpy as np
from numpy.random import Generator as gen 
from numpy.random import PCG64 as pcg

arr_gen=gen(pcg(seed=100))
print(arr_gen.normal(size=(5,5)))
print(arr_gen.integers(low=10, high=100,size=(5,5)))


import numpy as np
value=np.array([[2,3,4],[9,8,7]])
print(value[0])
print(value[1])
print(value[0,1])
print(value[1,2])
print(value[-2][-2])
print(value[-1,-2])

value1=np.array([[2,3,4],
                [6,7,8]])
value1[1,1]=55
print(value1)

value1[1]=7
print(value1)
value1[0]=6
print(value1)

list_value=[2,2,3,4,5,6,0]
list_value.append(7)
print(list_value)
list_value.insert(2,20)
print(list_value)
# list_value.clear()
# print(list_value)

list_value.pop(1)
list_value.pop()
print(list_value)

print(count_nonzero(list_value))
# count=0
# for item in list_value:
#     count+=1
#     print(item.as_integer_ratio())
# print(count)

# x=0.75
# print(x.as_integer_ratio())
# x=.50
# print(x.as_integer_ratio())

list_value=[2,2,3,4,5,6,0]
print(list_value.count(3))
list_value.sort()
print(list_value)

def binary_search(nums,target):
    n = len(nums)
    l = 0
    r = n - 1

    while l <= r:
        mid = (l + r) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1

    return -1
nums=[1,3,5,6]
target=5
print(binary_search(nums,target))


list_value=[10,'a',"abc",2.5,True]
# print(type(list_value))
print(list_value)

# ------------------------------
#tuple
tup_value=(1,2,3,4)
print(tup_value)
print(tup_value[0])
tup_value.index(2)
print(tup_value)

tup_value=(5,[6,7,3])
tup_value[1].append(8)
print(tup_value)

my_tuple=(1,2,3)#packing
a,b,c=my_tuple #unpacking
print(a)
print(b)
print(my_tuple[a])
print(my_tuple[b])
# my_tuple(1)=22
# print(my_tuple)


#add the tuple element
def addition(*numbers):
    print(type(numbers))
    my_tuple=0
    # for i in range(len(numbers)):
    for num in numbers:
        my_tuple+=num
    return my_tuple
        

res=addition(2,3,4,5)
print(res)

set_value={10,20,30,40,40}
# print(list(set_value))
print(set_value)
print()
if 20 in set_value:
    print("Yes")
    
a={1,2,3}
b={2,3,4}
print(a|b)
print(a&b)
print(a-b)

s={}
print(type(s))
s={None}
print(type(s))

student ={
    "name":"sachin",
    "age":24,
    "city":"bengaluru",
}
print(student["name"])

print(student.keys())
print(student.values())
print(student.items())
print(student.get("age"))
student.update({"age":25})
print(student)

dict_values={'first':1,'ele1':2,'ele2':20,'last':3}

for key,value in dict_values.items():
    if ((key!='first') & (key!='last')):
        # print(key,value)
        print(value)

x=10
print(id(x))
x=x+5
print(id(x))

list_value=[1,2,3]

print(id(list_value))
list_value[0]=100
print(list_value)
print(id(list_value))

# s="hello"
# s=s+ " world"
# print(s)

import copy
original=[[1,2,3],[4,5,6]]
shallow=copy.copy(original)
shallow[0][0]=100
print(original)
print(shallow)

import sys
a=[2,3,4]
b=a
print(sys.getrefcount(a))
del a
# print(a)
print(sys.getrefcount(b))

import gc

class A:
    pass


a=[1,2,3]
b=[1,2,3]
print(a==b)
#value are equal and they are diff objects in memory
print(id(a))
print(id(b))

a=[1,2,3]
# b=[1,2,3]
print(a is b)
a=b
print(a is b)

x=10
y=10
#caches the memory -5 to 256
print(x is y)

#== used for general comparison is used for None:

#*args and **kwargs
#it is functional to accept input as a variable number of arguments
#inside of the function it will become a tuple
#used to pass multiple positional arguments
def add(*args):
    return sum(args)
print(add(1,2,3,4,5))

#**kwargs
#it is used pass for the multiple named args

def print_info(**kwargs):
    print(kwargs)
print_info(name="sachin",age=25)


def demo(a, *args, **kwargs):
    print("a",a)
    print(args)
    print(kwargs)

demo(1,2,3,name="navi",city="bombay")

nums=[1,2,3,4]
res=list(map(lambda x:x*2,nums))
print(res)

nums=[1,2,3,4,5,6,7]
res=list(filter(lambda x: x%2==0,nums))
print(res)


#generator 
def count(num):
    i=1
    while i<=num:
        yield i
        i+=1
        
for num in count(4):
    print(num)
    
#asyncio

import asyncio

async def task1():
    await asyncio.sleep(2)
    print("Task 1 done")

async def task2():
    await asyncio.sleep(3)
    print("task 2 done")
    
async def main():
    await asyncio.gather(task1(),task2())
    
asyncio.run(main())


class Person:
    def __init__(self,name):
        self.name=name
    
    def greet(self):
        print(self.name)
        
p1=Person("Sachin")
p1.greet()

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    def display(self):
        print({self.name,self.marks})
s1=Student("ramu",90)  
s1.display()

#method using instance var

class BankAccount:
    def __init__(self,balance):
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
    def show_bal(self):
        print(self.balance)
        
b1=BankAccount(1000)
b1.deposit(200)
b1.show_bal()

class Employee:
    company="Prolims"
    
    def __init__(self,name):
        self.name=name
    
    def display(self):
        print(self.name,Employee.company)
    
e1=Employee("Amith")
print(e1.company)
print(e1.display) 

class Calculator:
    def add(self, a, b):
        return a + b
    
    def display(self, a, b):
        result = self.add(a, b)
        print("Result:", result)

c = Calculator()
c.display(5, 7)

#inheritance
class Animal():
    def speak(self):
        print("Animal speak")
class Dog(Animal):
    pass
d=Dog()
d.speak()

class Animal:
    def __init__(self,name):
        self.name=name
class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed
d1=Dog("Tommy","labrador")
print(d1.name,d1.breed)

class A:
    def showA(self):
        print("class A")
class B(A):
    def showB(self):
        print("class B")
class C(B):
    pass
obj=C() 
obj.showA()
obj.showB()     
        
#polymorphism
class Animal:
    def sound(self):
        print("animal sound")    
class Dog(Animal):
    def sound(self):
        print("dog is barking")
class Cat(Animal):
    def sound(self):
        print("pass")
animals=[Dog(),Cat(),Animal()]
for i in animals:
    i.sound()

#reverse a string without inbuilt
s1="Hello world"
s=list(s1)
l=0
r=len(s)-1
while l<=r:
    # temp=s[l]
    # s[l]=s[r]
    # s[r]=temp 
    s[r],s[l]=s[l],s[r]
    l+=1
    r-=1
print("".join(s))

for i in range(len(s)-1,-1,-1):
    print(s[i],end=" ")

#121
num=121
n=num
rev=0
while n>0:
    digit=n%10
    rev=(rev*10)+digit
    n//=10
if rev==num:
    print("palindrome")

#Find duplicate elements in list
list_values=['a','b','f','f','d']
duplicate=[]
for i in range(len(list_values)):
    for j in range(i+1,len(list_values)):
        if list_values[i]==list_values[j] and list_values[i] not in duplicate:
            duplicate.append(item)
        
print(duplicate)

#remove duplicate and print only unique
list_values=['a','b','f','f','d']
duplicate=[]
for item in list_values:
    if item not in duplicate:
        duplicate.append(item)
print(duplicate)

#find min
ar=[1,2,3,4,5]
min_val=ar[0]
for i in range(len(ar)):
    if ar[i]<min_val:
        min_val=ar[i]
print(min_val)

#Find second largest number
ar=[1,2,3,4,5]
max=float('-inf')
sec_max=float('-inf')
for i in range(len(ar)):
    if ar[i]>max:
        sec_max=max
        max=ar[i]
    elif ar[i]>sec_max and ar[i]!=max:
        sec_max=max
        
#count char freq
val="python"
freq={}
for ch in val:
    freq[ch]=freq.get(ch,0)+1
print(freq)


#Check anagram

def check_anagram(s1,s2):
    freq1={}
    freq2={}
    if len(s1) != len(s2):
        return 

    for ch in s1:
        freq1[ch]=freq1.get(ch,0)+1
    for ch in s2:
        freq2[ch]=freq2.get(ch,0)+1
        
    if freq1==freq2:
        print("anagram")
s1="silent"
s2="listen"
check_anagram(s1,s2)

#Sort a list without sort()


#insertion sort
def insert_sort(list_sort):
    
    for i in range(len(list_sort)):
        key=list_sort[i]
        j=i-1
        while j>=0 and list_sort[j]>key:
            list_sort[j+1]=list_sort[j]
            j-=1
        list_sort[j+1]=key
    return list_sort
list_sort=[1,3,2,4,5,6]
res=insert_sort(list_sort)    
print(res)
#selection sort
def selection_sort(list_sort):
    n=len(list_sort)
    for i in range(len(list_sort)-1):
        min_idx=i
        for j in range(i+1,n):
            if list_sort[j]<list_sort[min_idx]:
                min_idx=j
        temp=list_sort[min_idx]
        list_sort[min_idx]=list_sort[i]
        list_sort[i]=temp
    return list_sort
list_sort=[1,3,2,4,5,6,9]
res=selection_sort(list_sort)
print(res)

#bubble sort
def bubble_sort(nums):
    n=len(nums)
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if nums[j]>nums[j+1]:
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp
        return nums
    
list_sort=[1,3,2,4,5,6]
res=bubble_sort(list_sort)
print(res)



x=10
y=10
print(id(x))
print(id(y))
print(id(x)==id(y))

t=([1,2,3],4)
t[0].append(5)
print(t)

x=10
print(id(x))
x=x+5
print(id(x))
a=10
b=10
print(a==b)

print(a is b)
a=10
b=10
print(a is b)
print(id(a))
print(id(b))

a=10
b=10
print(a==b)

name="sachin"
print(id(name))
name=name.capitalize()
print(id(name))
print(name)

#mutable type list,set,dict,bytearray #memory address remains same
list=[1,2,3]
print(id(list))
list.append(4)
print(id(list))
print(list)

#dictionary
name={
    "name":"sachin",
    'city':25
}
print(name["name"],",",name["city"])

name["name"]="manu"
print(name)

# Difference between list, tuple, set, dict
#list ordered, mutable, duplicate, indexed based access the values

# list=[1,2,3,4,5]
# list.append(7)
# list.append(7)
# list[0]=99
# print(list)
# print(list[0])

#--------------
#tuple is a ordered, index, immutable, duplicate
t=(1,2,3,4,5,5)
print(t)
print(t[0])
print(t)

#set 
se={1,2,3,4,5}
set_val=set(se)
print(set_val)

#set
s={1,2,3,4,5,5}
s.add(8)
print(s)

#dict it has a key value pair, we can mute the value key must be unique,Ordered, mutable , access using the key
dict_value={
    "name":"sachin",
    "city":"mysore",
}

print(dict_value["name"])
dict_value["name"]="Naani"
print(dict_value["name"])
print(dict_value)


#shallow copy, create a new outer object, inner object are still referenced, only one level is copied

import copy
original=[[1,2],[3,4]]
print(id(original))
shallow=copy.copy(original)
print(id(shallow))
print(shallow)
shallow[1].append(5)
print(id(shallow))
print(shallow)

orig=[[1,2],[3,4]]
shallows=copy.copy(orig)
shallows[0].append(90)
print(orig)
print(shallows)


#deep copy
orig=[[1,2,3],[4,5]]
deep=copy.deepcopy(orig)
deep[0].append(8)
print(deep)
print(orig)

# ==
list1=[1,2,3]
list2=[1,2,3]
print(list1==list2) 
print(list1 is list2)
print(id(list1),id(list2))


a=10
b=10
print(a==b)
print(a is b)

a=1000000000000
b=1000000000000
print(a is b)

#immutable obj are pass by value
def modify(x):
    x=x+10
    print(x)
a=5
modify(a)
print(a)

def modify(lst):
    lst.append(900)
    print(lst)
    
list_value=[1,3,4,5]
modify(list_value)
print(list_value)


# *args it is used to pass multiple positional argument it collect argument into a tuple
def add_num(*args):
    return sum(args)
print(add_num(1,2,3,4))

#**kwargs
def display_info(**kwargs):
    print(kwargs)
display_info(name="sachin",city="hubli")

# #decorator
# def my_fun(fun):
#     def wrapper():
#         print("before function calling")
#         fun()
#         print('after function calling')
#     return wrapper
# @my_fun
# def say_hello():
#     print("hello")

# say_hello()

#decorator
def my_fun(fun):
    def wrapper():
        print("before calling")
        fun()
        print("after calling")
    return wrapper
@my_fun
def say_hello():
    print("hello")
say_hello()

#function with arguments
def my_fun(fun):
    def wrapper(*args, **kwargs):
        print("before calling")
        fun(*args, **kwargs)
        print("after calling")
    return wrapper
#in real project
from functools import wraps
def my_fun(fun):
    @wraps(fun)
    def wrapper(*args, **kwargs):
        print("before calling")
        res=fun(*args, **kwargs)
        print("after calling")
        return res
    return wrapper
    
add=lambda a,b : a+b
print(add(5,3))

# nums=[1,2,3,4,5]
# squared=list(map(lambda z:z*z, nums))
# print(squared)

# nums=[1,2,3,4,5,6]
# even=list(filter(lambda x:x%2==0, nums))
# print(even)

def count(n):
    i=1
    while i<=n:
        yield i
        i+=1
gen=count(3)
for num in gen:
    print(num,end=" ")
print()

nums=[1,2,3,4,5]
iterator=iter(nums) #it calls nums.__iter__()
print(next(iterator))

l_nums=[100,2,3,4,5]
val=l_nums.__iter__()
print(next(val))
print(next(val))
print(next(val))
print(next(val))
print(next(val))
# print(next(val))

nums=[1,2,3,4,5]
for num in nums:
    print(num)
    
#what python does internally
iterator=iter(nums)

while True:
    try:
        num=next(iterator)
        print(num)
    except StopIteration:
        break

#monkey patching
class monkey_patching:
    def fun_name(self):
        return "Hello"
m=monkey_patching()
print(m.fun_name())

def new_fun_name(self):
    return "Hey this is the patched method"
monkey_patching.fun_name=new_fun_name
print(m.fun_name())

#at the module level
import math
print(math.sqrt(16))
math.sqrt=lambda x: "patched"
print(math.sqrt(16))


class Test:
    def add(self,a,b,c=0):
        return a+b+c
obj=Test()
print(obj.add(2,3))
print(obj.add(2,3,5))

class Test:
    def add(self,*args):
        return sum(args)
obj=Test()
print(obj.add(2,3,4,5))


# What are dunder (magic) methods?
class Person:
    def __init__(self,name,city):
        self.name=name
        self.city=city
    def __str__(self):
        return f"{self.name}"
    
p=Person("sachhi","bombay")
print(p)

class MyList:
    def __init__(self,item):
        self.item=item
    def __len__(self):
        return len(self.item)
    
obj=MyList([1,2,3,4,5,6])
print(len(obj))


#encapsulation
# class BankAccount:
#     def __init__(self,balance):
#         self.__balance=balance #now this was private var
        
#     def deposit(self,amount):
#         self.__balance+=amount
        
#     def get_balance(self):
#         return self.__balance
    
    
# B_obj=BankAccount(10000)
# B_obj.deposit(5000)
# print(B_obj.get_balance())

class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
    
    def deposit(self,amount):
        self.__balance+=amount
        
    def get_balance(self):
        return self.__balance
b_obj=BankAccount(10000)
b_obj.deposit(2000)
print(b_obj.get_balance())

#abstraction
#hiding internal implementation and showing only the necessary functionality
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
c=Circle(5)
print(c.area())


#inheritance
class Animal:
    def speak(self):
        print("animal speak")
    
class Dog(Animal):
    def bark(self):
        print("dog is barking")
d=Dog()
print(d.bark())
print(d.speak())

#polymorphism
class Bird:
    def sound(self):
        return "sound"
class Dog:
    def sound(self):
        return "dog sound"
animals=[Bird(),Dog()]
for animal in animals:
    print(animal.sound())
for obj in [Bird(),Dog()]:
    print(obj.sound())
    
#multiple inheritance 

class Father:
    def skills(self):
        print("Teaching")
    
class Mother:
    def talent(self):
        print("painting")
class Child(Father,Mother):
    pass
c=Child()
print(c.skills())
print(c.talent())

class A:
    def show(self):
        return "a"
    
class B:
    def show(self):
        return "b"
    
class C(A,B):
    pass
obj=C()
print(obj.show())
print(C.__mro__)
print(C.mro())

class Parent:
    # def show(self):
    #     print("parent class")
    
    def __init__(self):
        print("parent class")
class Child(Parent):
    # def show(self):
    #     super().show()
    #     print("child class")
    def __init__(self):
        super().__init__()
        print("child class")
c=Child()

#classmethod and staticmethod
#classmethod it has arg is to be cls instead of self, access class variable
# a method that takes cls as a first argument instead of self argument
class Person:
    age=19
    def __init__(self,name):
        self.name=name
        Person.age+=1
    @classmethod
    def get_age(cls):
        return cls.age
p=Person("ram")
print(p.get_age())

#@staticmethod
class Math_util:
    @staticmethod
    def add(a,b):
        return a+b 
print(Math_util.add(2,3))   
        

#read the file 
# file=open("read.txt","r")
# content=file.read()
# print(content)
# file.close()

# with open("read.txt","r") as f:
#     content=f.read()
#     print(content)

#write to file
# with open("sample.txt","w") as f:
#     f.write("hello world")

#append to the file
# with open("sample.txt","a") as f:
#     f.write("\nNew line")

#if file does not exist in read mode it will raise the FileNotFoundError

# with open("file.txt","r") as f:
#     try:
#         content=f.read()
#         print(content)
#     except FileNotFoundError:
#         print("File not found!")

#remove the file 
# import os
# os.remove("sam.txt")

# from pathlib import Path
# file=Path("a.txt")
# if file.exists():
#     file.unlink()
#     print("file deleted")
#Hello world
# with open("file.txt","r") as f:
#     f.read(5)
#     print(f.tell())
#move pointer to the next position
#hello world
# with open("sample.txt","r") as f:
#     f.seek(6)
#     print(f.read())
    
#how to read a large file
# with open("sample.txt","r") as f:
#     for line in f:
#         print(line.strip())
        
# with open(".txt","r") as f:
#     while True:
#         line=f.readline()
#         if not line:
#             break
#         print(line.strip())
        
# import csv
# with open("file.txt","r") as f:
#     reader=csv.reader(f)
#     for raw in reader:
#         print(raw)
    
# import csv
# with open("file.txt","r") as f:
#     reader=csv.DictReader(f)
#     for raw in reader:
#         print(raw)

#how to write json data to the python file
# import json
# data={
#     "name":"sachin",
#     "city":"klbg",
#     "age":25,
# }

# with open("json_data.txt","w") as f:
#     json.dump(data,f)
    
#dump() write json to file
#dumps() write object to json string




