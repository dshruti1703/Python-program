a=int(input("enter 1 number :"))
b=int(input("enter 2 number :"))
def lcm(a,b):
    if a>b:
        greater = a
    else:
      greater = b 

    while (True):
        if (greater % a == 0) and (greater % b ==0):
            lcm=greater
            break
        greater +=1
    return lcm 

print ("lcm is " , lcm(a,b))
    