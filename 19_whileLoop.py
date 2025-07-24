count=1
while count<=5:
    print("Hello")
    count+=1

c=5
while c>=1:
    print(c)
    c-=1
    

p=1
while p<=100:
    print(p)
    p+=1

q=100
while q>=1:
    print(q)
    q-=1

# Multiplication
n=int(input("Enter number:-"))
j=1
while j<=10:
    print(n*j)
    j+=1

# Print element of the list using loops

l=[1,4,9,16,25,36,49,64,81,100]

m=1
while m<=len(l)-1:
    print("List items are:-",l[m])
    m+=1


# Key search
t=[1,4,69,16,25,36,49,64,81,100]
key=int(input("Enter Key:-"))

k=0
while k<len(t):
    if (t[k]==key):
        print("The key is:-",key,"in the index:-",k)
    else:
        print("The key is not present")
    k+=1