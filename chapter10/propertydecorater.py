class emp:
    a=1
    @classmethod
    def show(cls):
        print(f"the class value is :{cls.a} ")
    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    @name.setter
    def name(self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]
e=emp()
e.name="yash bora"
print(e.name)