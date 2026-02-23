class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
        
class SinglyLinkedList:
    def __init__(self,head=None):
        self.head=head
    def insertAtEnd(self,value):
        temp=Node(value)
        if(self.head!=None):
            t1=self.head
            while(t1.next!=None):
                t1=t1.next
            t1.next=temp
        else:
            self.head=temp

    def printLL(self):
        t1=self.head
        while(t1!=None):
            print(t1.data)
            t1=t1.next
obj=SinglyLinkedList()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.printLL()
            
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
a=Node(5)
b=Node(10)
c=Node(15)
# print(a.data)
# print(b.data)
# print(c.data)
a.next=b
b.next=c
head=a
print(head.data)
print(head.next.data)
print(head.next.next.data)

#traverse a linkedList
# def traverse_list(head):
curr=head
# while curr!=None:
while curr is not None:
    print(curr.data,end=" ")
    curr=curr.next
# traverse_list(head) 
print()

#traverse a linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
a=Node(1000)
b=Node(2000)
c=Node(3000)
a.next=b
b.next=c

head=a
curr=head
while curr is not None:
    print(curr.data,end="->")
    curr=curr.next
print("None")
        

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
a=Node(5)
b=Node(10)
c=Node(15)
a.next=b
b.next=c
head=a
curr=head
count=0
while curr!=None:
    count+=1
    curr=curr.next
print(count)
print()

class Node:
    def __init__(self,data):
        self.data=data
        self.next=next

a=Node(32)
b=Node(42)
c=Node(52)
a.next=b
b.next=c
head=a
curr=head
x=32
found = False
while curr is not None:
    if curr.data == x:
        found = True
        break
    curr = curr.next
print(found)


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
a=Node(5)
b=Node(10)
c=Node(15)
d=Node(20)
a.next=b
b.next=c
c.next=d
head=a
newNode=Node(2)
newNode.next=head
head=newNode
curr=head
while curr is not None:
    print(curr.data,end=" ")
    curr = curr.next

print()

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
a=Node(5)
b=Node(10)
c=Node(15)
a.next=b
b.next=c
head=a
curr=head
newNode=Node(6)
k=2
for i in range(k-1):
    curr = curr.next
newNode.next=curr.next
curr.next=newNode
temp=head
while temp:
    print(temp.data,end="->")
    temp=temp.next
print("None")
print()

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
a=Node(90)
b=Node(91)
c=Node(92)
d=Node(93)
a.next=b
b.next=c
c.next=d
head=a
if head is not None:
    head=head.next
curr=head
while curr is not None:
    print(curr.data,end="->")
    curr=curr.next
print("None")

#delete last node
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# a=Node(100)
# b=Node(200)
# c=Node(300)
# d=Node(400)
# a.next=b
# b.next=c
# c.next=d
# head=a
# curr=head
# while curr is not None:

#insertion at the beginning
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
a=Node(10)
b=Node(20)
c=Node(30)
a.next=b
b.next=c
head=a
newNode=Node(5)
newNode.next=head
head=newNode
curr=head
while curr is not None:
    print(curr.data,end="->")
    curr=curr.next
print("None")

#insertion at the end
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
a=Node(10)
b=Node(20)
c=Node(30)
a.next=b
b.next=c
head=a
newNode=Node(40)
curr=head
while curr.next is not None:
    curr=curr.next
curr.next=newNode
#print the updated list
curr=head
while curr is not None:
    print(curr.data,end="->")
    curr=curr.next
print("None")

nums=[1,2,3,4,5]
n=len(nums)
for i in range(-1,(-n-1),-1):
    print(nums[i],end=" ")
print()

x=-10
print(abs(x))


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
a=Node(50)
b=Node(51)
c=Node(52)
d=Node(53)

a.next=b
b.next=c
c.next=d

head=a

#reverse logic
curr=head
prev=None

while curr is not None:
    nxt=curr.next #store the next value
    curr.next=prev
    prev=curr
    curr=nxt
head=prev
curr=head
while curr is not None:
    print(curr.data,end="->")
    curr = curr.next
print("END")

res=[]
def list_value(data,res):
    #it's a dictionary
    if isinstance(data,dict):
        for k,v in data.items():
            res.append(k)
            list_value(v,res)
    #list
    elif isinstance(data,list):
        for i in data:
            list_value(i,res)
    else:
        res.append(data)


data={1:{2:[3,{4:5}],6:7},8:9}
list_value(data,res)
print(res)


res=[]   
def list_value(data,res):
    if isinstance(data,dict):
        #for dict
        for k, v in data.items():
            res.append(k)
            list_value(v,res)
    elif isinstance(data,list):
        for item in data:
            list_value(item,res)
    else:
        res.append(data)        

data={1:{2:[3,{4:5}],6:7},8:9}
list_value(data,res)
print(res)
        


        

        

        
    