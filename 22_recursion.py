# Recursive Function
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(5)


#Factorial Problems

def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)

f=fact(5)
print(f)