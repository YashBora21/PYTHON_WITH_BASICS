"""n=int(input("enter the number"))
for i in range(0,11):
    print(f"{n} X {i} = {n*i}")
"""

#writ ethe program in list for name satrt with s
"""
l = ["akash","abhi","shruti","ram","sujay"]

for i in l:
    if(i.endswith("i")):
        print(i)
"""
'''
#prime number
n= int(input("enter the number "))

for i in range (2,n):
    if(n%i) ==0 :
        print("it is not prime")
        break
else:
        print("it is  prime")
        '''
'''
n= int(input("enter the number "))
fact=1
for i in range(1,n+1):
   
    fact=fact*i
print(fact)

'''
#pattern 
"""  *
    ***
   *******
   """
 
"""
n= int(input("enter the number "))
for i in range(1,n+1):
  print(" "*(n-i),end="")
  print("*"* (2*i-1),end="")
  print("")
   """ """
n= int(input("enter the number "))
for i in range(1,n+1):
  if i==1 or i==n :
    print("*"*n)
  else:
    print("*",end="")
    print(" "*(n-2),end="")
    print("*",end="")
    print("")
"""
n= int(input("enter the number "))
for i in range(10,0,-1):
    print(f"{n} X {i} = {n*i}")
  