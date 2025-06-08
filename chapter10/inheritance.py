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