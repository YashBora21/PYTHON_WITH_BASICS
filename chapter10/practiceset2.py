'''class twodVector:
    def __init__(self,i,j) :
        self.i=i
        self.j=j

class threedVecotr(twodVector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k
    def show(self):
        print(f"the vector is: {self.i}i+{self.j}j+{self.k}k")

o1=threedVecotr(1,2,3)
o1.show()
'''
'''
class emp:
    salary=1234
    increment=21
    @property
    def salaryinc(self):
        return (self.salary+self.salary*(self.increment/100))
    @salaryinc.setter
    def salaryinc(self,salary):
        self.increment=((salary/self.salary)-1)*100

e=emp()
e.salaryinc=1493.1399999999999
print(e.increment)
'''
'''
#coomplex
class complex:
    def __init__(self,r,i):
        self.r=r
        self.i=i
    def __add__(self,c2):
        return complex(self.r+c2.r,self.i+c2.i)
    def __mul__(self,c2):
        real=self.r*c2.r - self.i*c2.i
        imj=self.r*c2.i+self.i*c2.r
        return complex(real,imj)
    def __str__(self):
        return f"{self.r} + {self.i}i"
    

c1=complex(1,2)
c2=complex(3,4)

print(c1*c2)
'''

#override len method
class vector:
    def __init__(self,l):
        self.l=l

    def __len__(self):
        return len(self.l)

v1=vector([1,2,3])
print(len(v1))
