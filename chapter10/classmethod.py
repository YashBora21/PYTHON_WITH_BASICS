class emp:
    a=1
    @classmethod
    def show(cls):
        print(f"the class value is :{cls.a} ")

e=emp()
e.a=45
e.show()