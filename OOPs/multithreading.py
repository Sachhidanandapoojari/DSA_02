import threading
import time

def task(name):
    print(f"task {name} starting")
    time.sleep(2)
    print(f"task {name} ended")
    
t1=threading.Thread(target=task, args=("A",))
t2=threading.Thread(target=task,args=("B",))
start=time.time()
t1.start()
t2.start()

t1.join()
t2.join()

print("Total time",time.time()-start)


import multiprocessing
import time

def task(name):
    print(f"task {name} starting")
    count=0
    for _ in range(1000000):
        count+=1
    print(f"task {name} finished")
    
p1=multiprocessing.Process(target=task,args=("A",))
p2=multiprocessing.Process(target=task,args=("B",))
start=time.time()

p1.start()
p2.start()

p1.join()
p2.join()

print("total time",time.time()-start)


# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def selection_sort(nums):
    n=len(nums)
    for i in range(n):
        min_val=nums[i]
        indx=i
        for j in range(i+1,n):
            if nums[j]<min_val:
                min_val=nums[j]
                indx=j
        temp=nums[i]
        nums[i]=nums[indx]
        nums[indx]=temp
    return nums
res=selection_sort([3,2,1,5,6,9,8,7])
print(res)
def find_prime(num):
    if num<1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
num=29
res=find_prime(num)
print(res)


arr=[1,2,3,4,5,6]
for i in range(len(arr)-1,-1,-1):
    print(arr[i],end=" ")

nums=[2,3,4,3,5,6,7]
freq={}
for i in range(len(nums)):
    freq[nums[i]]=freq.get(nums[i],0)+1
print(freq)

def is_Palindrome(s,l,r):
    if l>=r:
        return True
    if s[l]!=s[r]:
        return False
    return is_Palindrome(s,l+1,r-1)
s="mam"
print("palindrome" if is_Palindrome(s,0,len(s)-1) else "Not Palindrome")

def is_palindrome(s,l,r):
    if l>=r:
        return True
    if s[l]!=s[r]:
        return False
    return is_palindrome(s,l+1,r-1)
s="mam"
print("pali" if is_palindrome(s,0,len(s)-1) else "Not")


s="bob"
rev=""
for i in range(len(s)-1,-1,-1):
    rev=rev+s[i]
if rev==s:
    print("palindrome given string")
    
    



