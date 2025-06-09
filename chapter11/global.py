a=9 #gloabal variable
def fun():
    global a
    a=89
    print(a)


fun()
print(a)