#set is an collection of well defined objects
# to create empty set
d=set()
s={0,1,3,4,4,2,"hrr"}
print(s)#it cannot repeat elements
s.add(23)
print(s)
print(len(s))
s.remove("hrr")
print(s)
s2={1,23,1,343,12}
print(s.union(s2))
print(s.intersection(s2))
print(s2.intersection(s))
print(s-s2)
print(s2-s)
print({1,2}.issubset(s))
print(s2.issuperset(s))