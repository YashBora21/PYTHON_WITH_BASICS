'''
f=open("yassh.txt","r")
data=f.read()
print(data)
f.close()
'''
#this can be  done same without writting f.close()

with open("yassh.txt") as f:
    print(f.read())