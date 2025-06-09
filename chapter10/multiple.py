class emp:
    company="itc"
    def show(self):
        print(f"the name is {self.company}  ")

class coder:
    language="php"
    def printlang(self):
        print(f"the language is :{self.language}")

class programmer(emp,coder):
    company="itc infotech"
    def showdetail(self):
        print(f"the name is {self.company}  the language is :{self.language} ")

a=emp()
b=programmer()
b.show()
b.printlang()
b.showdetail()