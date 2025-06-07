# dictionary in python
d={}#empty dict
marks={
    "yash":100,
    "a":200,
    "c":100
}
#print(marks[0]) we cant acess this like 
print(marks["c"])
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"a":120,"ha":120})
print(marks)
print(marks.get("a")) #if key dosent match it gives null as it is differ than direct acessing mathod
marks.pop("ha")
print(marks)
