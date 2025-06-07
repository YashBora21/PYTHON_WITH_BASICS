def fact(a):
    if a==0 or n==1:
        return 1
    return a*fact(a-1)


n=int(input("enter teh number :"))
print("fact is",fact(n))