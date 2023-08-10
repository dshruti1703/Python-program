def add (x,y):
    return x+y
def sub (x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
x=int(input("enter 1 number :"))
y=int(input("enter 2 number :"))
value=int(input("Enter a number from 1/2/3/4 : "))
if value==1: 
    print('Addition is' , add(x,y))
elif value ==2:
    print('sub is' , sub(x,y))
elif value==3:
    print('Addition is' , multiply(x,y))
else:
    print(divide(x,y))