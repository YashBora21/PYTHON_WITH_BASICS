import random 
a=-1
n=random.randint(1,100)
guesse=0
while (a!=n):
    guesse+=1
    a=int(input("guess the number: "))

    if(a>n):
        print("lower number please")

    else:
        print("higher number please ")
print(f"great you geusees in attempt:{guesse}")