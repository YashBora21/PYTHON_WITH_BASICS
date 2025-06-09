#use to not to crash program if it gets error
try:
    a=int(input("hey ,enter the number"))
    print(a)
except ValueError as e:
    print("eerror spotted")
    print(e)
except Exception as e:
    print(e)
print("thankyou")