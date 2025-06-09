class emp:
    a=1
    @classmethod
    def show(cls):
        print(f"the class value is :{cls.a} ")

e=emp()
e.a=45#using class method wee directly use class atrribut not object 
#sso ti print 1

e.show()