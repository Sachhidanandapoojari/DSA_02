class Dog:
    species = "Canis familiaris" 
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def bark(self):
        print(f"dog {self.name}")
        print(self.species)
d=Dog("Bruno", 3)
d.bark()

# class Dog:
#     def bark(self):
#         return f"dog {self.name}"
# d=Dog()
# d.name="Bruno"
# print(d.bark())

# class Dog:
        
#     def bark(this):
#         return f"dog {this.name}"
# d=Dog()
# d.name="Mudhol"
# print(d.bark()) 

class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def bark(self):
        return f"Dog{self.name}"
d=Dog("mudhol",3)
print(d.bark())

class Dog:
    def bark(this,name):
        return f"dog{this.name}"
d=Dog()
d.name="whitetiger"
res=d.bark(d)
print(res)

class Employee:
    company="prolims"
    count=0
    
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.count+=1
    
    
e=Employee("Ram",80000)
print(e.company)
print(Employee.count)


class Dog:
    tricks=[]
    
    def add_trick(self,trick):
        self.tricks.append(trick)
d1=Dog()
d2=Dog()
d1.add_trick("roll over")
d2.add_trick("sit")
print(d1.tricks)
print(d2.tricks)

# ✅ Fix — use instance variable
class Dog:
    def __init__(self):
        self.trick=[]
    
    def add_trick(self,tricks):
        self.trick.append(tricks)
d1=Dog()
d2=Dog()
d1.add_trick("Hey")
d2.add_trick("hi")
print(d1.trick)
print(d2.trick)

#var order
class MyClass:
    x=10
obj=MyClass()
obj.x=99
print(obj.x)
print(MyClass.x)
del obj.x
print(obj.x)
        

class MyClass:
    class_var="this is the class var"
    
    def __init__(self,value):
        self.value=value
    #instance method work with instance data
    def instance_method(self):
        print(f"{self.value} and {self.class_var}")
    #instance method inside we can access the class_var and self.val
    
    # 2. CLASS METHOD — works with class data
    @classmethod
    def class_method(cls):
        return f"{cls.class_var}" #classmethod access only class data not instance
    
    #static method is independent not work class as well as instance
    @staticmethod
    def static_method(x,y):
        return x+y
    #no self and no cls
    
obj = MyClass(42)
inst_data=obj.instance_method()
class_method=MyClass.class_method()
print(class_method)
print(MyClass.static_method(3,4))


class Date:
    def __init__(self,day,month,year):
        self.day,self.month,self.year=day,month,year
    
    @classmethod
    def from_string(cls,date_string):
        day,month,year =map(int, date_string.split("-"))
        return cls(day,month,year)
    @classmethod
    def today(cls):
        import datetime
        t=datetime.date.today()
        return (t.day,t.month,t.year)
d=Date.from_string("15-08-2024")
d=Date.today()
print(d)

import datetime
t=datetime.date.today()
print(t.today())

class MathHelper:
    @staticmethod
    def find_prime(n):
        if n<2:
            return False
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
res=MathHelper.find_prime(11)
print(res)


#encap
class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner 
        self._balance=balance #protected
        self.__pin=1234 #private
        
    def deposit(self,amount):
        if amount>0:
            self._balance+=amount
    def withdraw(self,amount):
        if amount>self._balance:
            raise ValueError("insuff fund")
        self._balance -= amount
    def get_bal(self):
        return self._balance
b=BankAccount("ram",20000)
b.owner
b.get_bal
b.deposit
# b.BankAccount__pin


class Circle:
    def __init__(self,value):
        self._value=value #protected
    @property              #getter
    def radius(self):
        return self._value
    @radius.setter
    def radius(self,value):
        if value<0:
            raise ValueError("")
        self._value=value
    
    #for the computation no needed the property
    @property
    def calc_radius(self):
        import math
        return math.pi * self._value**2
c=Circle(5)
c.radius=10
print(c.calc_radius)

#abstraction
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    def describe(self):
        return f"{self.area():.2f}"
    

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
        
    def area(self):
        import math
        return math.pi ** self.radius**2
    
    def perimeter(self):
        import math
        return 2*math.pi*self.radius
    


#inheritance
class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        return f"{self.name}"   
    def speak(self):
        return "sound"
    
class Dog(Animal):
    def __init__(self,name,age,breed):
        super().__init__(name,age)
        self.breed=breed
    
    def speak(self):
        return super().speak()
    
    def fetch(self):            # new method
        return f"{self.name} fetches the ball!"
d = Dog("Bruno", 3, "Labrador")
print(d.eat())
print(d.speak()) 
print(d.fetch())


#polymorphism
class Animal:
    def speak(self):
        return f"....."
class Dog:
    def speak(self):
        return f"Woof!"

class Cat:
    def speak(self):
        return "meow"
animals=[Animal(),Dog(),Cat()]
for animal in animals:
    print(animal.speak())
    
#operator overloading

class Vector:
    def __init__(self,x,y):
        self.x,self.y=x,y
        
    def __add__(self, other):
        return Vector(self.x+other.x,self.y+other.y)
    def __str__(self):
        return f"{self.x,self.y}"
v1=Vector(1,4)
v2=Vector(2,5)
print(v1+v2)

class Parent:
    def greet(self): return "Hello from Parent"

class Child(Parent):
    def greet(self): return "Hello from Child"  # overrides
    
class MyClass:
    def greet(self): return "no args"
    def greet(self, name): return f"Hello {name}"
    
obj = MyClass()
# obj.greet()  

#mro save the ambiguity and create the diamond shape and resolve the ambiguity || super method follow the MRO
class A:
    def hello(self):
        return "A"
class B(A):
    def hello(self):
        return "B"
class C(A):
    def hello(self):
        return "c"
class D(B,C): #multiple inheritance
    pass

d=D()
print(d.hello())
print(D.__mro__)
print(D.mro()) 






    
        
    
    
    
        
    
    
    
        
        
        
        
        
        
        
    
    
    
        
        


        


        
        
    
        
        
        
    

        
        
        
     