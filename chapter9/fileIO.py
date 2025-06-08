'''
f= open("yassh.txt","w")
data="hi my self yash "
f.write(data)

f.close()'''
'''
f=open("yassh.txt","r")
data=f.read()
print(data)
f.close()
'''
'''
f=open("yassh.txt","r")
#lines=f.readlines() list 
line1=f.readline()
line2=f.readline()
print(type(line1))#string
print(line1,line2,)
f.close()
'''
f= open("yassh.txt","a")
data="appended "
f.write(data)
f.close()