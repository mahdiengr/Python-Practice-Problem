def add(num1,num2):
    n=int(num1)
    n2=int(num2)
    return n + n2

def sub(num1,num2):
    
    n=int(num1)
    n2=int(num2)
    if(n>n2):
        return n - n2
    else:
        return n2 - n

def multi(num1,num2):
    n=int(num1)
    n2=int(num2)
    return n * n2

def div(num1,num2):
    n=int(num1)
    n2=int(num2)
    if(n>n2):
        return n/n2
    else:
        return n2/n
  
n1=int(input("Enter 1st Number:"))
n2=int(input("Enter 2nd Number:"))
print("Add Number: ",add(n1,n2))
print("Subtraction : ",sub(n1,n2))
print("Multification: ",multi(n1,n2))
print("Divided ", div(n1,n2))
