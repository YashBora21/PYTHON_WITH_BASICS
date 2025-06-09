class employee:
    company="infotech"
    def get(self,name,salary,language):
        self.name=name
        self.salary=salary
        self.language=language
      #  print(f"the name is {self.name} and the salary is {self.salary}")

class programmer(employee):

    def show(self):
        print(f"the name is {self.name} and the salary is {self.salary} and laangauage is {self.language}")


'''class softwaredev:
    company="infotech pune"
    def show(self):
        print(f"the name is {self.name} and the salary is {self.salary}")'''

obj=programmer()
obj.get("harsh",10000,"php")
obj.show()

'''
class Employee:
    company = "infotech"
    
    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language

class Programmer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary, language)  # calls parent class constructor

    def show(self):
        print(f"The name is {self.name}, salary is {self.salary}, language is {self.language}")

'''