#function definition 
def avg(a,b,c=2):
    avg=((a+b+c)/3)
    return avg
#function call 
a=avg(2,9)
print("the avg is",round(a,2))