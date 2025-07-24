nums={4,5,6,2,3,1}
print(nums)
print(type(nums))

nums2=set()
print(nums2)
print(type(nums2))

# Mehods
s=set()
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)
print(s)
print(len(s))

s.remove(5)
print(s)
print(len(s))

s.pop()
print(s)
print(len(s))

s.clear()
print(s)
print(len(s))

# union
set1={1,2,3,4}
set2={3,4,5,6}

print(set1.union(set2))

# Intersection
print(set1.intersection(set2))