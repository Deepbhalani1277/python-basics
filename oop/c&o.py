class Person:
    name= "Deep"
    occupation = "Student"
    networth = 0
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person()
a.name = "maitri"
a.occupation = "student"
a.info()
#self means current obj which is being called
#for ex here in b.Person() "self" will be "b"

b = Person()
b.name = "Het"
b.occupation = "Accountant"
b.info()