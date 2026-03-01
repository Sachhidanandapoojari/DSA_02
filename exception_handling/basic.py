try:
    res=10/0
except ZeroDivisionError:
    print("Can't divide by zero")
except (TypeError,ValueError) as e:
    print("type error or value error {e}")
except Exception as e:
    print(f"Something went wrong: {e}")
else:                                   # runs ONLY if NO exception
    print(f"Result: {res}")
finally:
    print("Cleanup done")
import sys   
# try:
#     sys.exit()
# except Exception:
#     print("exce")
    
try:
    sys.exit()
except BaseException:
    print("baseexce")
conn=None    
# with get_db_connection() as conn:
#     res=conn.execute("selct * from user") #auto closed
# get_db_connection()   

# try:
#     x=10/0
# except DatabaseError as e:

def func():
    try:
        return 1
    except:
        return 2
    else:
        return 3
    finally:
        return 4

print(func())
# import json
# try:
#     json.loads("individual json")
# except json.JSONDecodeError as e:

try:
    res=1/0
except Exception:
    print("general")
except ZeroDivisionError:
    print("specific")


from array import *
val=array('d',[1,2,3,4,4,5,5.3])
print(val)
# reversed(val)
val.reverse() #return none and original modify and inplace it will do modify 
print(val)

val=array('d',[1,2,3,4,4,5,5.3])
res=reversed(val)
print(res)
print(list(res))

list_value=[1,2,4,5,6,7,8]
list_value.reverse()
print(list_value)

res=reversed(list_value)
print(res)
print(list(res))
list_value=[1,2,4,5,6,7,8]
res=list_value.pop(2)
print(res)
list_value=[1,2,4,5,6,7,8]
list_value.pop()
print(list_value)

list_value.append(100)
print(list_value)

array_value=array('i',[12,23,4,5,6,76,87])
print(array_value[:4])
print(array_value[:-5])


print(array_value[::-1])
print(array_value[3:5])
print(array_value[2:])
print(array_value[:2])
print(array_value[3:-1])
print(array_value[3:6])

arr=[1,2,3,4,5,6]
for i in range(-1,-(len(arr))-1,-1):
    print(arr[i],end=" ")
print()  

arr1=[1,2,3,4,5,6]
arr=list(arr1)
l=0
r=len(arr)-1
while l<r:
    temp=arr[l]
    arr[l]=arr[r]
    arr[r]=temp
    l+=1
    r-=1
print(arr)

s1="We promptly judged antique ivory buckles for the next prize"
s=s1.lower()
letter=set()
for ch in s1:
    if "a"<=ch<="z":
        letter.add(ch)
if len(letter)==26:
    print("panagram")
else:
    print("not")

str_value="Sachin poojari "
res=str_value.strip().lower().replace(" ","")
print(res) 

s="Sachin poojari "
print(s.lower().strip().replace(" ",""))  

#check anagram 

def find_anagram(s,t):
    if len(s)!=len(t):
        return False
    freq1={}
    freq2={}
    for ch in s:
        freq1.get(ch,0)+1
    for ch in t:
        freq2.get(ch,0)+1
    return freq1==freq2
    
s="silent"
t="listen"
print(find_anagram(s,t))

#reverse the word
s="the sky is blue"
words=s.split()
print(len(words))
rev=reversed(words)
# print(str(list(rev)))
# print(rev)
print("".join(rev))

s1 = "Hello World"
s=s1.split()
rev=s[::-1]
print(" ".join(rev))

#extract a digit given in integer

num = 123456
while num>0:
    digit=num%10
    print(digit,end=" ")
    num//=10
print(num)

# nums=[1,2,3,4]
# nums.push(10)
# print(nums)

s="Hello\\tPython\\nworld"
word_list=s.split()
print(word_list)
    
    
def gen_yield(n):
    yield n
n=[1,2,3,4]
print(list(gen_yield(n)))

def add_nums(*args):
    return sum((args))
print(add_nums(1,2,3,4))

def add_num(**kwargs):
    return kwargs
print(add_num(name="sachin",age=22))

def example(*args, **kwargs):
    print(args)
    print(kwargs)
example(1,2,3,name="john",age=23)

import threading
import time
def task(name):
    print(f"task {name}is starting")
    time.sleep(10)
    print("task ended")
t1=threading.Thread(target=task,args=("A",))
t2=threading.Thread(target=task,args=("B",))
start=time.time()
t1.start()
t1.join()
print(time.time()-start)

from multiprocessing import Process
import time
def task(name):
    print(f"{name} started the processing")
    count=0
    for _ in range(10000):
        count+=1
    print(f"task {name} finished")
    
p1=Process(target=task,args=("a",))
start=time.time()
p1.start() #execution of the thread
p1.join() # wait the main thread until child thread execution #with out join may the main thread execute before function ending

print(time.time()-start)


#check palindrome
num=121
# l=0
# r=len(num)-1
# n=len(num)
temp=num
rev=0
while temp>0:
    reminder=temp%10
    rev=(rev*10)+reminder
    temp//=10
if rev==num:
    print("palindrome")
else:
    print("not")
    
s1="madam"
s=list(s1)
l=0
r=len(s)-1
while l<r:
    s[r],s[l]=s[l],s[r]
    l+=1
    r-=1
if "".join(s)==s1:
    print("palindrome")
    
#check armstrong number

n=153
# print(len(str(n)))
n=len(str(n))
# num=n
# total=0
# while n>0:
#     rem=num%10
#     total=total+(rem**n)
#     num//=10
# print(total)

#print factors of all the given num using brute force 20=1,2,4,5,10

nums=20
res=[]
for i in range(1,nums+1):
    if nums%i==0:
        res.append(i)
print(res)
num=10
res=[]
for i in range(1,(num//2)+1):
    if num%i==0:
        res.append(i)
print(res)
        
    
s1="hello world"
# word=s.split()
# print("".join(wor))
s=list(s1)
res=[]
for ch in s:
    if ch!=' ':
        res.append(ch)
print("".join(res))

s1 = "hello world"  # remove the duplicate letter
seen=[]
for ch in s1:
    if ch not in seen:
        seen.append(ch)
print("".join(seen))

nums=[1,2,3,4,4,5,6,7,8,9]
seen=set()
duplicate=[]
# for i in num:
#     if num[i]==num[i-1]:
#         duplicate.append(i)
#     seen.add(i)
# print(seen)

nums=[1,2,3,4,4,5,6,7,8,9]
unique=[]
for i in range(len(nums)):
    if nums[i] not in unique:
        unique.append(nums[i])
print(unique)

nums=[1,2,3,4,4,5,6,7,8,9]
seen=set()
for num in nums:
    if num not in seen:
        seen.add(num)
print(seen)

nums=[1,2,3,4,4,5,6,7,8,9]
seen=set()
duplicate=[]
for num in nums:
    if num not in seen:
        seen.add(num)
        duplicate.append(num)
print(seen)
# print(duplicate)

nums=[1,2,3,4,4,5,6,7,8,9] #print only duplicate
res=[]
for i in range(len(nums)):
    if nums[i]==nums[i-1]:
        res.append(nums[i])
print(res)

import math
a=10
b=20
print(math.gcd(a,b))

def gcd(a,b):
    res=1
    for i in range(1,min(a,b)+1):
        if a%i==0 and b%i==0:
            res=i
    return res
print(gcd(20,40))


def insertion_sort(num):
    n=len(num)
    for i in range(1,n):
        key=num[i]
        j=i-1
        while j>=0 and num[j]>key:
            num[j+1]=num[j]
            j-=1
        num[j+1]=key
    return num
num=[3,2,4,5,6,1,7]
print(insertion_sort(num))

def bubble_sort(nums):
    n=len(nums)
    for i in range(n):
        isSwaped = False
        for j in range(n-i-1):
            if nums[j]>nums[j+1]:
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp
                isSwaped = True
        if not isSwaped:
            break
    return nums
nums=[3,2,4,5,6,1,7]
print(bubble_sort(nums))

def selection_sort(num):
    n=len(num)
    for i in range(n):
        min=num[i]
        indx=i
        for j in range(i+1,n):
            if num[j]<min:
                min=num[j]
                indx=j
        temp=num[i]
        num[i]=num[indx]
        num[indx]=temp
    return num
            
    
num=[3,2,4,5,6,1,7]
print(selection_sort(num))


class Merge_Sort_Solution:
    
    def merge(self,nums,l,mid,r):
        a=[]
        b=[]
        for i in range(l,mid+1):
            a.append(nums[i])
        for j in range(mid+1,r+1):
            b.append(nums[j])
        
        i,j,k=0,0,l
        while k<=r:
            if j==len(b):
                nums[k]=a[i]
                i+=1
                k+=1
                
            elif i==len(a):
                nums[k]=b[j]
                j+=1
                k+=1
                
            elif a[i]<b[j]:
                nums[k]=a[i]
                i+=1
                k+=1
            else:
                nums[k]=b[j]
                j+=1
                k+=1
                
    
    def merge_sort(self,nums,l,r):
        if l<=r:
            return 
        mid=(l+r)//2
        self.merge_sort(nums,l,mid)
        self.merge_sort(nums,mid+1,r)
        
        self.merge(nums,l,mid,r)
        
nums=[5, 2, 8, 9, 3, 7, 4]
m=Merge_Sort_Solution()
m.merge_sort(nums,l,len(nums)-1)
print(nums)


class Merge_sort_solution:
    def merge(self,nums,l,mid,r):
        a=[]
        b=[]
        for i in range(l,mid+1):
            a.append(nums[i])
        for i in range(mid+1,r):
            b.append(nums[i])
        
        i,j,k=0,0,l
        while k<=r:
            if j==len(b):
                nums[k]=a[i]
                i+=1
                k+=1
            elif i==len(a):
                nums[k]=b[i]
                j+=1
                k+=1
            elif a[i]<b[j]:
                nums[k]=a[i]
                i+=1
                k+=1
            else:
                nums[k]=b[j]
                j+=1
                k+=1
                
    def merge_sort(self,nums,l,r):
        if l<=r:
            return 
        mid=(l+r)//2
        self.merge_sort(nums,l,mid)
        self.merge_sort(nums,mid+1,r)
        
        self.merge(nums,l,mid,r)
        
nums=[5, 2, 8, 9, 3, 7, 4]
m=Merge_sort_solution()
m.merge_sort(nums,l,len(nums)-1)
print(nums)

class Merge_Sort_Solution:

    def merge(self, nums, l, mid, r):
        a = nums[l:mid+1]
        b = nums[mid+1:r+1]

        i, j, k = 0, 0, l
        while k <= r:
            if j == len(b):
                nums[k] = a[i]
                i += 1
            elif i == len(a):
                nums[k] = b[j]
                j += 1
            elif a[i] <= b[j]:
                nums[k] = a[i]
                i += 1
            else:
                nums[k] = b[j]
                j += 1
            k += 1

    def merge_sort(self, nums, l, r):
        if l >= r:
            return
        mid = (l + r) // 2
        self.merge_sort(nums, l, mid)
        self.merge_sort(nums, mid+1, r)
        self.merge(nums, l, mid, r)


nums = [5, 2, 8, 9, 3, 7, 4]
m = Merge_Sort_Solution()
m.merge_sort(nums, 0, len(nums)-1) 
print(nums)  # [2, 3, 4, 5, 7, 8, 9]


# class QuickSort:
#     def partition(self,num,l,r):
#         #write the swapping tech
#         start=l
#         key=num[r]       
#         for i in range(l,r+1):
#             if num[i]<=key:
#                 temp=num[i]
#                 num[i]=num[start]
#                 num[start]=temp
#                 start+=1
#         return start-1         
        
#     def quickSort(self,num,l,r):
#         if l>=r:
#             return
#         p=self.partition(num,l,r)
        
#         self.quickSort(num,l,p-1)
#         self.quickSort(num,p+1,r)
# q=QuickSort()
# num=[7,2,8,1,3,6,4]
# q.quickSort(num,0,len(num)-1)
# print(num)    

class QuickSort:
    
    def partition(self,nums,l,r):
        #write the swapping 
        start=l
        key=nums[r]
        for i in range(l,r+1):
            if nums[i]<=key:
                temp=nums[i]
                nums[i]=nums[start]
                nums[start]=temp
                start+=1
        return start-1
    
    def quickSort(self,nums,l,r):
        if l>=r:
            return
        # mid=(l+r)//2
        p=self.partition(nums,l,r)
        self.quickSort(nums,l,p-1)
        self.quickSort(nums,p+1,r)
        
nums=[7,2,3,6,5,4,8]   
q=QuickSort()
q.quickSort(nums,0,len(nums)-1)
print(nums)

class LinearSearch:
    def search(self,nums,target):
        for i in range(0,len(nums)):
            if nums[i]==target:
                return i
        return -1

nums=[2,3,4,5,6]
target=3    
obj=LinearSearch()
res=obj.search(nums,target)
print(res)

# arr_val=list(map(int(input("enter the array"))))
# print(arr_val)

#remove dup from the list
list_val=[1,2,2,3,4,5,5,6]
seen=set()
res=[]
for val in list_val:
    if val not in seen:
        seen.add(val)
        res.append(val)
print(res)

#frequency of the array in dictionary
arr=[5,6,6,7,8,9,4,5,6,2]
freq={}
for i in range(0,len(arr)):
    freq[arr[i]]=freq.get(arr[i],0)+1
print(freq)

s10="madam"
s1=list(s10)
l=0
r=len(s1)-1
while l<=r:
    temp=s[l]
    s[l]=s[r]
    s[r]=temp
    l+=1
    r-=1
if "".join(s1)==s10:
    print("palindrome")
    
def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)
print(factorial(4))

#fibo
def fibonacci(n):
    if n==0 or n==1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(4))

# with open("file.txt","r") as f, open("file.txt","w") as fr:
#     data=f.read()
#     fw=fr.write(data.upper())
    
    
import csv

# data = [
#     ["Name",  "Age", "City"],
#     ["Raj",    25,   "Mumbai"],
#     ["Priya",  22,   "Delhi"],
# ]
# with open("user.csv","w",newline="") as fc:
#     writer=csv.write(fc)
#     writer.writerows()
    

# #reading csv
# with open("file.txt","r") as fr:
#     read=csv.reader(f)
#     readf=next(read) #skips the header rows
#     for row in readf:
#         print(row)
        
# # DictReader — rows as dicts (most useful)
# with open("file.txt","r") as fr:
#     reader=csv.DictReader(fr)
#     for row in reader:
#         print(row["Name"])

# import json
# data = {
#     "name": "Raj",
#     "age": 25,
#     "skills": ["Python", "Django"],
#     "active": True
# }

# with open("file.json","w") as fw:
#     json.dump(fw,indent=4)  #dict to json file directly write
    
# json_str=json.dumps(data,indent=4)
# print(json_str)
# print(type(json_str))

#dump dict to json file directly write it 
#dumps dict to json string
#json.load() json file to dict
#json.loads() json string to dict 


#read json 
# with open("file.json","r") as fr:
#     loaded=json.load(fr)
#     print(loaded["Name"])

# json_str = '{"name": "Raj", "age": 25}'
# res=json.loads(json_str)
# print(res)

# try:
#     with open("data.txt", "r") as f:
#         data = f.read()
# except FileNotFoundError:
#     print("File doesn't exist")
# except PermissionError:
#     print("No permission to access it")
# except IsADirectoryError:
#     print("That's a directory, not a file")
# except OSError as e:
#     print(f"OS error: {e}")
# # Checking if file exists before opening
# import os
# if os.path.exists("data.txt"):
#     with open("data.txt", "r") as f:
#         read=f.read()
        
    


# class MyThread(threading.Thread):
#     def __init__(self,name):
#         super().__init__()
#         self.name=name
    
#     def run(self):   # override run() not start()!
#         print({self.name})
#         time.sleep(1)
#         print({{self.name}})
# t=MyThread("coding")
# t.join()
# t.start()








    













        
    

  


        











        






    

    

    
    



    

    
        
    




        


    
    

    