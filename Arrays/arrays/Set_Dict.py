s={1,2,3,4,5,5}
print(type(s))
s.add(10)
print(s)
set1={"Hey",1,2,3,4,5,"Sachin","Hey"}
print(set1)
set1.remove(2)
print(set1)

if 2 in set1:
    print(True)
else:
    print(False)
set1.discard(5)
print(set1)
print()

# set3={1,2,3}
# set4=set3.copy  
# # set4=set3
# set3.add(23)
# print(set3)

# set1={1,2,3}
# set2=set1.copy()
# set2.add(4)
# print(set1)
# print(set2)
# print(id(set1))
# print(id(set2))

    
#deepcopy
# import copy
# list1=[[1,2,3],[5,6,7]]
# list2=copy.deepcopy(list1)
# list1[0].append(99)
# print(list1)
# print(list2)
# print(id(list1))
# print(id(list2))

#deepcopy using set

# set1={1,2,4}
# set2=copy.deepcopy(set1)
# set1.add(5)
# print(set1)
# print(set2)


#Deep Copy with List inside a List
import copy
list1=[[1,2,3],[4,5]]
list2=copy.deepcopy(list1)
print(id(list1))
print(id(list2))
list1[0].append(90)
print(list1)
print(list2)


list1=[[1,2,3],[4,5]]
list2=list1.copy()
# print(id(list1))
# print(id(list2))
# list2.append(20)
list2[0].append(90)
print(list1)
print(list2)

#Shallow Copy with Set
set1={1,2,3,4}
set2=set1.copy()
set2.add(30)
set1.add(90)
print(id(set1),set1)
print(id(set2),set2)

#union and intersections


# print(set1|set2)
# print(set1.union(set2))
# print(set1&set2)
set1={1,2,3,4,5}
set2={6,7,8,8,9}
print(set1.intersection(set2))


#difference
set11={1,2,3,4,5,6}
set12={0,2,0,3,3,3}
print(set11-set12)

set20={2,3,5}
set21={8,9,2,3}
print(set20.intersection(set21))

print(set20.symmetric_difference(set21))

dict={}
print(type(dict))
dict1={1:"Sachin","Hello":89,90.0:'hey'}
print(dict1.keys())
print(dict1.values())
dict_values={
    1:"hey",
    2:"Sachin",
}
print(dict_values.keys())
# dict_values.clear()
print(dict_values)
print(dict_values[1])
print(dict_values)

dict_values[3]="Yash"
print(dict_values)
dict_values.update({1:"Ram"})
print(dict_values)
dict_values[1]="Ramu"
print(dict_values)

dict_values.pop(2)
print(dict_values)

del dict_values[3]
print(dict_values)

dict_values[2]="navya"
print(dict_values)
dict_values.get(0)
print(dict_values)

dict1={1:"Sachin","Hello":89,90.0:'hey'}
dict2=dict1.copy()
dict2[1000]="Ramu"
print(dict1)
print(dict2)

print(dict1.items())
for key, value in dict1.items():
    print(key,value)
    
for key in dict1.keys():
    print(key)
for value in dict1.values():
    print(value)




#find the frequency of the element present in the list

list=["abhinav","ram","sachin","lava","ram"]
freq={}
for name in list:
    if name not in freq:
        freq[name]=1
    else:
        freq[name]+=1
print(freq)

s="physics wallah skills"
freq={}
for ch in s:
    if ch not in freq:
        freq[ch]=1
    else:
        freq[ch]+=1
print(freq)

s="physics wallah skills"
freq={}
for ch in s:
    freq[ch]=freq.get(ch,0)+1
print(freq)






        
    




