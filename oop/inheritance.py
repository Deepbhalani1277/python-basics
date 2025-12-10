class Empolyee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def ShowDetails(self):
        print(f"Employee Name: {self.name}, Employee ID: {self.id}")

class programmer(Empolyee):
    def showlang(self, lang):
        print(f"Employee Name: {self.name}, Employee ID: {self.id}, Language: {lang}")

emp = Empolyee("Deep", 101)
emp.ShowDetails()
prog = programmer("Maitri", 102)
prog.showlang("Python")