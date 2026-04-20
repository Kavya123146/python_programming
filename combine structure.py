#combine structure
class Employee:
    def __init__(self,name):
        self.name=name
    def works(self):
        print("employe's Do the work")
class manager(Employee):
    def work(self):
        print(self.name,"The manager manages the team")
class Tester(Employee):
    def work(self):
        print(self.name,"The tester tests the code")
def Employee_details(emp):
    emp.work()
m=manager("girls")
T=Tester("boys")
Employee_details(m)
Employee_details(T)
        
