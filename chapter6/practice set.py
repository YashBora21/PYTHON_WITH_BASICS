# 1
"""""
a=int(input("enter tbe number"))
b=int(input("enter tbe number"))
c=int(input("enter tbe number"))
d=int(input("enter tbe number"))

if(a>b and a>b and a>c and a>d):
    print("greater is :",a)
elif(b>a and b>c and b>d):
    print("grreater is:",b)
elif(c>a and c>b and c>d):
    print("grreater is:",b)
else:
    print("greater is :",d)  """""
'''
b=int(input("enter tbe marks"))
c=int(input("enter tbe marks"))
a=int(input("enter tbe marks"))
if (a>33 and b>33 and c>33 and ((a+b+c)*100/300) >40):
    print("pass")
else:
    print("fail") '''
'''
#spam protection
p1 = "make money"
p2 = "scam"
p3 = "giveaway"
p4 = "gift"

msg =input("etner the comment:")

if((p1 in msg) or (p2 in msg) or (p3 in msg) or p4 in msg):
    print("delete comments")
else:
    print("accept")  '''

l=["ak","ag","af","ds"]
name = input("enter the name :")
if name in l :
    print("your name in")
else:
    print("not in list ")
