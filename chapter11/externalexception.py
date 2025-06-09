
a=int(input("hey ,enter the number"))
b=int(input("hey ,enter the number"))
if(b==0):
    raise ZeroDivisionError("hey you not divide by zero")
else:  
    print(f"the answer of divison is{a/b}")
