marks=[52,85,45,68]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])



# Slicing
print(marks[2:4])
print(marks[:3])
print(marks[2:])
print(marks[-3:-1])

# Methods

print(marks.append(25))
print(marks)
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)
marks.reverse()
print(marks)
marks.insert(2,36)
print(marks)
marks.remove(36)
print(marks)
marks.pop(25)
print(marks)