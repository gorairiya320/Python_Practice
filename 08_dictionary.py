info={
    "key":"value",
    "name":"Riya",
    "Roll":26
}
print(info)
print(type(info))
print(info["name"])
info["age"]=24
print(info)

#Nesting
stu={
    "Name":"Riya",
    "subjects":{
        "bengali":40,
        "English":30
    }
}
print(stu)

print(stu["subjects"]["English"])

# Mehods
myDic={
    "name":"riya",
    "Roll":26,
    "price":50.63
}

print(myDic.keys())
print(myDic.values())
print(myDic.items())
print(myDic.get("price"))
