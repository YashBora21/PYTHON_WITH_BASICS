#to translate hindi words

words={
    "madad":"help",
    "hath":"hand",
    "gend":"ball"
}
word=input("enter the word to transalate :")
print("here's your word ",words[word])

# same int and char in set
s={"15",15}
print(s)
s.add(15.0)
print(s)#15.0 same as 15

s=set()
d={}
print(type(s))

print(type(d))

#chage the value  entered later will be updated
s={4,3,4,"har",[1,2]}
# we cannot include list in set TypeError: unhashable type: 'list'
print(type(s))


