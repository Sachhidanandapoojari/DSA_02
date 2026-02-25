# import threading
# def task():
#     print("thread running")
# t1=threading.Thread(target=task())
# t1.start()
# t1.join()

# import threading
# import time
# def task():
#     time.sleep(2)
#     print("Task completed")
# t1=threading.Thread(target=task)
# t1.start()
# t1.join()  # Main thread waits here
# print("program finished")

import threading
import time
def task():
    time.sleep(10)
    print("Task completed")
t1=threading.Thread(target=task)
t1.start()
t1.join() #main thread waits here
print("program finished")

def back_ground_task():
    print("backgound task running")
    time.sleep(1)
t1=threading.Thread(target=back_ground_task)
t1.daemon=True #set as a daemon thread
t1.start()
time.sleep(3)
print("main thread executing")


# from multithreading import threading
# from multiprocessing import Process

# def task():
#     print("process running")
    
# p=Process(target=task)
# p.start()
# p.join()

from multiprocessing import Process
def task():
    print("process running")
    
p=Process(target=task)
p.start()
p.join()



# Reverse string
s1="sachin"
s=list(s1)
l=0
r=len(s)-1
while l<=r:
    temp=s[l]
    s[l]=s[r]
    s[r]=temp
    l+=1
    r-=1
print("".join(s))

s1="sachinpoojari"
s2=list(s1)
for i in range(len(s2)-1,-1,-1):
    print("".join(s2[i]),end="")
print()
# Find duplicate in array
arr=[1,2,3,4,4,5]
duplicate=[]
for i in range(len(arr)):
    if arr[i]==arr[i-1]:
        duplicate.append(arr[i])
print(duplicate)

arr=[1,2,3,4,4,5]
duplicate=[]
for i in range(len(arr)):
    if arr[i] not in duplicate:
        duplicate.append(arr[i])
print(duplicate)

arr=[1,3,4,4,5,6,7]
a=list(set(arr))
print(a)

#move zero to the end of the array
arr=[1,3,4,4,5,6,7,0,0,5,8,0,7]
temp=[]
for i in range(0,len(arr)):
    if arr[i]!=0:
        temp.append(arr[i])
for i in range(len(temp)):
    arr[i]=temp[i]
for i in range(len(temp),len(arr)):
    arr[i]=0
print(arr)
from array import array 
array_value=array('i',[1,2,3,4,5])
print(array_value[:3])
print(array_value[::-1])
print(array_value)
print(array_value[2:])
print(array_value[2:-1])
#check panagram
s="We promptly judged antique ivory buckles for the next prize"
s1=s.lower()
letter=set()
for ch in s1:
    if 'a'<=ch<='z':
        letter.add(ch)
if len(ch)==26:
    print("panagram")        
else:
    print("not")   
        
s1="listen".lower().strip().replace(" ","")
s2="silent".lower().strip().replace(" ","")
if len(s1)!=len(s2):
    print("not anagram")
else:
    freq1={}
    freq2={}
    for ch in s1:
        freq1[ch]=freq1.get(ch,0)+1
    for ch in s2:
        freq2[ch]=freq2.get(ch,0)+1
    if freq1==freq2:
        print("anagram")

s="the sky is blue"
words=s.split()
words.reverse()
print("".join(words))

#reverse number
num=123
n=num
rev=0
while n>0:
    digit=n%10
    rev=(rev*10)+digit
    n//=10
print(rev)

# num= 121
num= 121
n=num
rev=0
while n>0:
    digit=n%10
    rev=(rev*10)+digit
    n//=10
if num==rev:
    print("palindrome")
else:
    print("not")
    
st="madams"
s=list(st)
l=0
r=len(s)-1
while l<r:
    s[r],s[l]=s[l],s[r]
    l+=1
    r-=1
print("".join(s))

#find missing number
arr=[1,2,3,5,6,7]
n=len(arr)+1
expected_sum=n*(n+1)//2
actual_sum=sum(arr)
print(expected_sum-actual_sum)

#find second largest    
arr=[1,2,3,5,6,7]
n=len(arr)
first_max=arr[0]
second_max=arr[0]
for i in range(n):
    if arr[i]>first_max:
        second_max=first_max
        first_max=arr[i]
    elif arr[i]>second_max and arr[i]!=first_max:
        first_max=second_max
print(second_max)

#fib series
def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1)+fib(n-2)
res=fib(3)
print(res)
    
# from functools import lru_cache
# @lru_cache
# def fib(n):
#     if n==0 or n==1:
#         return n
#     return fib(n-1)+fib(n-2)
# print(fib(10))

#fib series
from functools import lru_cache
@lru_cache
def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1)+fib(n-2)
print(fib(10))


# def Is_Prime(n):
#     if n<=1:
#         return False
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True
# res=Is_Prime(7)
# print(res)

def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
res=is_prime(7)
print(res)
import json

data={
    "name":"Sachin",
    "city":"mumbai",
}
print(type(data))
#dict to json
res=json.dumps(data)
print(res)
print(type(res))

#dump the json 
import json
data={"name":"sachin","city":"mohali"}

with open("data.json","w") as f:
    json.dump(data,f)
    
#header are key value pair sent with http request or response it contain metadata extra information about the data


