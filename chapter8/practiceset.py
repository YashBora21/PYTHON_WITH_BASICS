'''def great(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c ): 
        return b
    else:
        return c
print("greatest is ",great(3,9,1)) '''
"""
def recur(n):
    if  n==0:
        return 0
    return n+recur(n-1)

a=int(input("enetr the number :"))
print("sum",recur(a))"""

def patern(a):
    if a==0:
        return 0
    print("*"*a,end="")
    print("")
    patern(a-1)

b=int(input("enter the  num:"))
patern(b)