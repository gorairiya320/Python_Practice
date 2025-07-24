#Function definiton
def sum(a,b):#Arguments
    return a+b

# Function call
s=sum(5,5)#Parametrs
print(s)


def avg(a,b,c):
    sum=a+b+c
    avg=sum/3
    print(avg)

avg(10,20,30)
avg(562,96,158)


#default parameter
def mul(a,b=10):
    print(a*b)

mul(5)


name=["riya","piya","shibu"]
roll=[26,27,28,29,30]

def list_len(list):
    print(len(list))

list_len(name)
list_len(roll)

#Factorial Function

def fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
        print(fact)

fact(5)


def find_evenodd(n):
    if(n%2==0):
        print("Even!")
    else:
        print("Odd!")

find_evenodd(10)
find_evenodd(9)