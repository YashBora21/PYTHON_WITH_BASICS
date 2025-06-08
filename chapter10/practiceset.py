#stor information of programmer working forn microsoft
'''
class programmer:
    company="microsoft"
    def __init__(self,name,salary):
        self.name=name 
        self.salary=salary

obj=programmer("rohan",10000)
print(obj.name,obj.salary)    
'''
import random
class train:
    def book(self,train_no,fro,to):
        print(f"ticket is booked in train no {train_no}  from {fro} to {to}")

    def getstatus(self,train_no):
         print(f"ticket is booked in train no {train_no} is runnig on time ")

    def getfare(slef,train_no,fro,to):
        print(f"ticket fare is of train no {train_no}  from {fro} to {to} is  {random.randint(1000,1500)}")

t=train()
t.book(1231,"pune","jaipur")
t.getstatus(1231)
t.getfare(1231,"pune","jaipur")