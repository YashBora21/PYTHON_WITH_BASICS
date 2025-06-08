'''
class employee:
    Name="xyz"
    language="hindi"

obj=employee()
obj.salary=100000
print(obj.Name,obj.language,obj.salary)
#here name and language are class attribue and slaary is object attritbute
'''
class employee:
    def __init__(self,a,b):
       print("gm great to se you")
       print(f"name is:{a} and language is {b}")
'''      def  getdata(self,a,b):
      print(f"name is:{a} and language is {b}")
  
    @staticmethod
    def greed():
       print("goood morning ... honey ")'''


obj=employee("xyz","hindi")
#obj.getdata()
#obj.greed()
