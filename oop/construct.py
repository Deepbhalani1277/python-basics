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