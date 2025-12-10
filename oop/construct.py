#constructor

'''
class Person:
 
    # name = "deep"
    # occ = "student"
    #in place of creating parameters like this we can use constructor 
    
    def __init__(self, n, o):
        self.name = n
        self.occ = o

    def info(self):#when writing any method self is medatory
        print(f"{self.name} is {self.occ}")
    
a = Person("deep","Student")
b = Person("Het","HR")
# a.name = "vishwa"
# a.occ = "HR"

a.info()
b.info()
# print(f"name{a.name}")
# print(f"occ{a.occ}")

'''

#decorators
'''

def greet(func):
    def wrapper():
        print("Good Morning")
        func()
        print("Have a nice day")
    return wrapper
@greet
def hello():
    print("Hello Deep")

def add(a,b):
    return a+b

hello()

'''

#getters and setters
'''

class MyClass:
    def __init__(self,value):
        self._value = value

    def show(Self):
        print(f"Value is {Self._value}")

    def get_value(self):
        return self._value
    def set_value(self, value):
        self._value = value

obj = MyClass(10)
obj.show()  
obj.set_value(20)
obj.show()

'''
    
class Employee:
    def __init__(self, name, id):
        self._name = name
        self._id = id

    def ShowDetails(self):
        print(f"Employee Name: {self._name}, Employee ID: {self._id}")

e = Employee("Deep", 101)
e.ShowDetails()
e._name = "Vishwa"  # Direct access (not recommended)
e._id = 102        # Direct access (not recommended)
e.ShowDetails()
